#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
AdaptiveSkewDetector — основной детектор перекоса волатильности для Hunter 6.0.

Использует Isolation Forest с онлайн-обновлением для обнаружения аномалий в опционном skew.
Поддерживает опциональное квантовое усиление (QuantumSkewDetector).
"""

import logging
import numpy as np
import pandas as pd
from typing import Optional, Dict, Any, Tuple
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
from datetime import datetime, timedelta

# Импорт квантового детектора (если доступен)
try:
    from .quantum_detector import QuantumSkewDetector
    QUANTUM_AVAILABLE = True
except ImportError:
    QUANTUM_AVAILABLE = False
    logging.warning("QuantumSkewDetector не найден. Квантовое усиление отключено.")

logger = logging.getLogger(__name__)


class AdaptiveSkewDetector:
    """
    Адаптивный детектор перекоса волатильности.

    Параметры:
        contamination: float, ожидаемая доля аномалий (по умолчанию 0.05)
        n_estimators: int, число деревьев в Isolation Forest
        max_samples: int или float, размер подвыборки
        random_state: int, seed
        lookback: int, окно для вычисления скользящих статистик
        use_quantum: bool, использовать ли квантовое ядро (требуется QuantumSkewDetector)
        quantum_config: str, путь к конфигу квантового детектора
        quantum_weight: float, вес квантового сигнала при комбинировании (0..1)
        threshold: float, порог anomaly score для генерации сигнала
    """

    def __init__(
        self,
        contamination: float = 0.05,
        n_estimators: int = 100,
        max_samples: float = 0.8,
        random_state: int = 42,
        lookback: int = 30,
        use_quantum: bool = False,
        quantum_config: Optional[str] = None,
        quantum_weight: float = 0.3,
        threshold: float = -0.5,
    ):
        self.contamination = contamination
        self.n_estimators = n_estimators
        self.max_samples = max_samples
        self.random_state = random_state
        self.lookback = lookback
        self.threshold = threshold
        self.use_quantum = use_quantum and QUANTUM_AVAILABLE
        self.quantum_weight = quantum_weight
        self.quantum_config = quantum_config

        # Isolation Forest
        self.iso_forest = IsolationForest(
            contamination=contamination,
            n_estimators=n_estimators,
            max_samples=max_samples,
            random_state=random_state,
            warm_start=True,  # позволяет добавлять новые данные
        )
        self.scaler = StandardScaler()
        self.is_fitted = False

        # Квантовый детектор (опционально)
        self.quantum_detector = None
        if self.use_quantum:
            if quantum_config is None:
                raise ValueError("Для квантового режима необходимо указать quantum_config")
            self.quantum_detector = QuantumSkewDetector(
                config_path=quantum_config,
                lookback=lookback,
                threshold=threshold,
                use_quantum=True,
            )
            logger.info("QuantumSkewDetector инициализирован.")

        # История для онлайн-обучения
        self.X_history = []          # накопленные признаки
        self.y_history = []          # метки (норма/аномалия) для возможного дообучения
        self.max_history = 10000     # ограничение на размер истории

        # Статистика
        self.last_signal_time = None
        self.signal_count = 0

    def _extract_features(self, market_data: Dict[str, Any]) -> np.ndarray:
        """
        Извлекает признаки из рыночных данных для детектора.

        Ожидается, что market_data содержит как минимум:
            - 'underlying_price': float
            - 'option_skew_25d': float (skew 25-delta)
            - 'term_structure': float (разница между ближней и дальней волатильностью)
            - 'volume_ratio': float (отношение текущего объёма к среднему)
            - 'funding_rate': float (для фьючерсов)
            - 'open_interest_change': float (изменение OI)
            - 'order_book_imbalance': float (дисбаланс стакана)

        Возвращает вектор признаков (1D numpy array).
        """
        # Базовые признаки
        features = {
            'skew': market_data.get('option_skew_25d', 0.0),
            'term': market_data.get('term_structure', 0.0),
            'vol_ratio': market_data.get('volume_ratio', 1.0),
            'funding': market_data.get('funding_rate', 0.0),
            'oi_change': market_data.get('open_interest_change', 0.0),
            'imbalance': market_data.get('order_book_imbalance', 0.0),
            'price_change': market_data.get('price_change_1h', 0.0),
            'iv_rank': market_data.get('iv_rank', 0.5),  # имплицитная волатильность ранг
        }
        # Можно добавить скользящие средние, если есть история
        # (здесь упрощённо)
        return np.array(list(features.values()), dtype=np.float32)

    def _combine_scores(self, classical_score: float, quantum_score: Optional[float] = None) -> float:
        """
        Комбинирует классический и квантовый scores в один итоговый.
        Чем меньше score, тем более аномально.
        """
        if quantum_score is None or not self.use_quantum:
            return classical_score
        # Взвешенная сумма (нормализовать к одному масштабу)
        # Предполагаем, что quantum_score имеет примерно тот же диапазон, что и classical_score
        # (classical_score из Isolation Forest: отрицательные значения для аномалий)
        combined = (1 - self.quantum_weight) * classical_score + self.quantum_weight * quantum_score
        return combined

    def fit(self, historical_data: pd.DataFrame) -> None:
        """
        Обучает детектор на исторических данных.

        historical_data: DataFrame с колонками, необходимыми для извлечения признаков.
                         Должен содержать временной индекс.
        """
        # Преобразуем историю в признаки
        features_list = []
        for _, row in historical_data.iterrows():
            # Преобразуем строку в словарь (упрощённо: считаем, что row — это словарь)
            market_dict = row.to_dict()
            feat = self._extract_features(market_dict)
            features_list.append(feat)

        X = np.array(features_list)
        if X.shape[0] == 0:
            raise ValueError("Нет данных для обучения")

        # Масштабирование
        X_scaled = self.scaler.fit_transform(X)

        # Обучение Isolation Forest
        self.iso_forest.fit(X_scaled)
        self.is_fitted = True

        # Сохраняем историю для онлайн-обновления
        self.X_history = X_scaled.tolist()
        self.y_history = [1] * X_scaled.shape[0]  # считаем все нормальными

        # Если используется квантовый детектор — обучаем его на тех же данных
        if self.use_quantum and self.quantum_detector is not None:
            try:
                self.quantum_detector.train(historical_data)
                logger.info("Квантовый детектор обучен на исторических данных.")
            except Exception as e:
                logger.error(f"Ошибка обучения квантового детектора: {e}")
                self.use_quantum = False  # отключаем квантовый режим при ошибке

        logger.info(f"AdaptiveSkewDetector обучен на {X.shape[0]} образцах")

    def update_online(self, market_data: Dict[str, Any], is_anomaly: bool = False) -> None:
        """
        Онлайн-обновление модели новыми данными (инкрементальное обучение).

        market_data: текущие рыночные данные
        is_anomaly: если True, помечаем как аномалию (для возможного переобучения)
        """
        if not self.is_fitted:
            logger.warning("Модель не обучена, вызов fit() игнорируется.")
            return

        feat = self._extract_features(market_data)
        feat_scaled = self.scaler.transform(feat.reshape(1, -1))
        self.X_history.append(feat_scaled.flatten())
        self.y_history.append(-1 if is_anomaly else 1)

        # Ограничиваем размер истории
        if len(self.X_history) > self.max_history:
            self.X_history = self.X_history[-self.max_history:]
            self.y_history = self.y_history[-self.max_history:]

        # Дообучаем Isolation Forest с warm_start
        # Для простоты используем весь накопленный набор (можно оптимизировать)
        X_batch = np.array(self.X_history)
        self.iso_forest.fit(X_batch)
        logger.debug(f"Модель обновлена онлайн, размер истории: {len(self.X_history)}")

    def detect(self, market_data: Dict[str, Any]) -> Tuple[bool, Dict[str, Any]]:
        """
        Основной метод детекции.

        Возвращает:
            signal: bool, True если обнаружена аномалия (сигнал на вход в Long Strangle)
            metrics: dict с дополнительной информацией
        """
        if not self.is_fitted:
            raise RuntimeError("Детектор не обучен. Вызовите .fit() сначала.")

        # Извлечение признаков и масштабирование
        feat = self._extract_features(market_data)
        feat_scaled = self.scaler.transform(feat.reshape(1, -1))

        # Классический score (Isolation Forest)
        classical_score = self.iso_forest.score_samples(feat_scaled)[0]
        classical_pred = self.iso_forest.predict(feat_scaled)[0]  # 1 or -1

        # Квантовый score (если включён)
        quantum_score = None
        quantum_metrics = {}
        if self.use_quantum and self.quantum_detector is not None:
            try:
                q_score, q_metrics = self.quantum_detector.detect(market_data)
                quantum_score = q_score
                quantum_metrics = q_metrics
            except Exception as e:
                logger.error(f"Ошибка квантового детектора: {e}")
                # при ошибке используем только классический

        # Комбинированный score
        combined_score = self._combine_scores(classical_score, quantum_score)

        # Генерация сигнала (если score ниже порога)
        signal = combined_score < self.threshold

        # Сбор метрик для логирования и отладки
        metrics = {
            'timestamp': datetime.utcnow().isoformat(),
            'classical_score': classical_score,
            'classical_prediction': classical_pred,
            'quantum_score': quantum_score,
            'combined_score': combined_score,
            'threshold': self.threshold,
            'signal': signal,
            'quantum_metrics': quantum_metrics,
        }

        # Дополнительная статистика
        if signal:
            self.signal_count += 1
            self.last_signal_time = datetime.utcnow()

        return signal, metrics

    def set_threshold(self, new_threshold: float) -> None:
        """Изменяет порог чувствительности."""
        self.threshold = new_threshold
        if self.quantum_detector:
            self.quantum_detector.set_threshold(new_threshold)
        logger.info(f"Порог изменён на {new_threshold}")

    def get_stats(self) -> Dict[str, Any]:
        """Возвращает статистику работы детектора."""
        return {
            'is_fitted': self.is_fitted,
            'use_quantum': self.use_quantum,
            'history_size': len(self.X_history),
            'signal_count': self.signal_count,
            'last_signal_time': self.last_signal_time.isoformat() if self.last_signal_time else None,
            'threshold': self.threshold,
        }

  Пояснения
Полная обратная совместимость — если use_quantum=False (по умолчанию), поведение не меняется.

Квантовый детектор инициализируется, если use_quantum=True и указан quantum_config. Он обучается на тех же исторических данных, что и основной детектор.

Комбинирование — итоговый combined_score является взвешенной суммой классического и квантового scores. Вес quantum_weight можно настраивать (по умолчанию 0.3).

Онлайн-обновление — метод update_online позволяет дообучать модель на новых данных с пометкой аномальности.

Гибкость — все параметры передаются через конструктор.

Использование
python
from aria.hunters.hunter6 import AdaptiveSkewDetector

# Создание с квантовым усилением
detector = AdaptiveSkewDetector(
    contamination=0.05,
    use_quantum=True,
    quantum_config="configs/quantum/base.yaml",
    quantum_weight=0.4,
    threshold=-0.6,
)

# Обучение на исторических данных (DataFrame)
detector.fit(historical_df)

# В торговом цикле
signal, metrics = detector.detect(current_market_data)
if signal:
    # Открыть позицию Long Strangle
    ...
