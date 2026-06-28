"""Квантовый детектор перекоса волатильности для Hunter 6.0."""

import numpy as np
import pandas as pd
from typing import Optional, Tuple
import logging

from aria.quantum import AnomalyEngine, FinancialDomainAdapter

logger = logging.getLogger(__name__)

class QuantumSkewDetector:
    """
    Обнаруживает аномалии в опционном перекосе с использованием квантового ядра.
    Может работать как альтернатива Isolation Forest.
    """
    
    def __init__(
        self,
        config_path: str,
        lookback: int = 30,
        threshold: float = -0.5,  # порог anomaly score
        use_quantum: bool = True,
    ):
        self.engine = AnomalyEngine.from_config_file(config_path)
        self.adapter = FinancialDomainAdapter(lookback=lookback)
        self.threshold = threshold
        self.use_quantum = use_quantum
        self.is_trained = False
    
    def train(self, historical_data: pd.DataFrame, fund_rates: Optional[pd.Series] = None,
              oi: Optional[pd.Series] = None, skew: Optional[pd.Series] = None):
        """
        Обучает квантовый детектор на исторических данных (только нормальные рыночные режимы).
        """
        X = self.adapter.ingest(historical_data, fund_rates, oi, skew)
        # Используем только первые 70% как "норма"
        train_size = int(0.7 * len(X))
        X_train = X[:train_size]
        self.engine.fit(X_train)
        self.is_trained = True
        logger.info("QuantumSkewDetector обучен на %d образцах", len(X_train))
    
    def detect(self, market_data: dict) -> Tuple[float, dict]:
        """
        Принимает текущие рыночные данные и возвращает:
        - anomaly_score (чем ниже, тем более аномально)
        - метрики для отладки
        """
        if not self.is_trained:
            raise RuntimeError("Детектор не обучен. Вызовите .train() сначала.")
        
        # Преобразуем market_data в DataFrame (ожидается структура как в адаптере)
        # Здесь предположим, что market_data содержит OHLCV, и опционально funding, OI, skew
        # Для упрощения создаём DataFrame из переданных значений
        # В реальном коде — более сложная логика
        
        # Пример:
        df = pd.DataFrame({
            'open': market_data.get('open', [0]),
            'high': market_data.get('high', [0]),
            'low': market_data.get('low', [0]),
            'close': market_data.get('close', [0]),
            'volume': market_data.get('volume', [0]),
        })
        # Если есть дополнительные ряды, передаём их в adapter.ingest
        X_current = self.adapter.ingest(
            df,
            fund_rate=market_data.get('funding_rate'),
            oi=market_data.get('open_interest'),
            option_skew=market_data.get('skew')
        )
        # X_current — последняя строка (1-образец)
        score = self.engine.score_samples(X_current)[0]
        # Прогноз (1 или -1)
        pred = self.engine.predict(X_current)[0]
        
        # Дополнительные метрики
        metrics = {
            'quantum_score': score,
            'prediction': pred,
            'threshold': self.threshold,
            'is_anomaly': pred == -1,
            'signal_strength': abs(score)  # сила сигнала
        }
        return score, metrics
    
    def set_threshold(self, new_threshold: float):
        self.threshold = new_threshold
