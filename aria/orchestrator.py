#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
ARIA Orchestrator — автономный цикл Plan → Act → Reflect → Revise.

Управляет всеми агентами, интегрирует квантовый детектор,
обеспечивает самовосстановление и непрерывное обучение.
"""

import asyncio
import logging
import json
import sys
from datetime import datetime, timedelta
from typing import Dict, Any, Optional, List
from pathlib import Path

# Импорт компонентов ARIA
from aria.hunters.hunter6 import AdaptiveSkewDetector, QuantumSkewDetector, Executor, Hedger, PositionManager
from aria.quantum import AnomalyEngine, QuantumReflection
from aria.memory.odab_note import OdabNote          # предположим, что есть модуль памяти
from aria.memory.vibe_check import VibeCheck        # мета-когнитивный контроль
from aria.self_healing.reflection_loop import ReflectionLoop  # авто-коррекция
from aria.knowledge.knowledge_compiler import KnowledgeCompiler  # compile-time RAG

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("logs/orchestrator.log"),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger("orchestrator")


class AriaOrchestrator:
    """
    Главный оркестратор ARIA.
    Запускает бесконечный цикл: сбор данных → анализ → исполнение → рефлексия → исправление.
    """

    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.running = False
        self.cycle_count = 0
        self.max_cycles = config.get("max_cycles", None)  # None = бесконечно

        # Инициализация компонентов
        self._init_components()

        # Хранение последних результатов
        self.last_trade_results = []
        self.metrics_history = []

    def _init_components(self):
        """Инициализация всех агентов и сервисов."""
        # 1. Память и знания
        self.odab_note = OdabNote(storage_path="data/odab_note.db")
        self.vibe_check = VibeCheck(threshold=0.7)  # предотвращает перепроектирование
        self.reflection_loop = ReflectionLoop(odab_note=self.odab_note)
        self.knowledge_compiler = KnowledgeCompiler(source_dirs=["src/", "agents/"])

        # 2. Торговые детекторы (классический + квантовый)
        self.classical_detector = AdaptiveSkewDetector(
            contamination=self.config.get("contamination", 0.05),
            use_quantum=False,   # классический режим
            threshold=self.config.get("threshold", -0.5)
        )

        self.quantum_detector = None
        if self.config.get("use_quantum", False):
            self.quantum_detector = QuantumSkewDetector(
                config_path=self.config.get("quantum_config", "configs/quantum/base.yaml"),
                lookback=self.config.get("lookback", 30),
                threshold=self.config.get("threshold", -0.5),
                use_quantum=True
            )
            # Обучаем квантовый детектор на исторических данных (если есть)
            historical_data = self._load_historical_data()
            if historical_data is not None:
                self.quantum_detector.train(historical_data)
                logger.info("Квантовый детектор обучен.")

        # 3. Исполнители
        self.executor = Executor(
            exchange_config=self.config.get("exchange", {}),
            dry_run=self.config.get("dry_run", True)
        )
        self.hedger = Hedger(
            exchange_config=self.config.get("exchange", {}),
            delta_target=0.0
        )
        self.position_manager = PositionManager(
            max_daily_loss=self.config.get("max_daily_loss", 0.01),
            take_profit=self.config.get("take_profit", 0.5),
            stop_loss=self.config.get("stop_loss", -0.3)
        )

        # 4. Квантовая рефлексия (если включена)
        self.quantum_reflection = None
        if self.config.get("use_quantum", False) and self.quantum_detector is not None:
            self.quantum_reflection = QuantumReflection(
                engine=self.quantum_detector.engine,
                odab_note=self.odab_note
            )

        # 5. Загрузка начального состояния
        self._load_state()

    def _load_historical_data(self) -> Optional[Any]:
        """Загружает исторические данные из источника (Alpha Vantage / CCXT)."""
        # Здесь должна быть реальная загрузка через MCP.
        # Для примера — возвращаем None (будет использована синтетика при обучении)
        return None

    def _load_state(self):
        """Восстанавливает состояние из файла (если есть)."""
        state_path = Path("data/orchestrator_state.json")
        if state_path.exists():
            with open(state_path, 'r') as f:
                state = json.load(f)
                self.cycle_count = state.get("cycle_count", 0)
                self.last_trade_results = state.get("last_trade_results", [])
                logger.info(f"Состояние восстановлено, цикл #{self.cycle_count}")

    def _save_state(self):
        """Сохраняет текущее состояние для восстановления после перезапуска."""
        state = {
            "cycle_count": self.cycle_count,
            "last_trade_results": self.last_trade_results[-100:],  # последние 100
            "timestamp": datetime.utcnow().isoformat()
        }
        with open("data/orchestrator_state.json", 'w') as f:
            json.dump(state, f, indent=2)

    # ------------------------------------------------------------
    #  Основной цикл
    # ------------------------------------------------------------

    async def run(self):
        """Запускает бесконечный автономный цикл."""
        self.running = True
        logger.info("🚀 ARIA Orchestrator запущен. Начинаю охоту.")

        while self.running:
            try:
                self.cycle_count += 1
                logger.info(f"--- Цикл #{self.cycle_count} ---")

                # 1. Observe (сбор данных)
                market_data = await self._observe()

                # 2. Orient (построение контекста, RAG)
                context = await self._orient(market_data)

                # 3. Decide (принятие решений)
                decision = await self._decide(market_data, context)

                # 4. Act (исполнение)
                trade_result = await self._act(decision, market_data)

                # 5. Reflect (анализ и обучение)
                reflection = await self._reflect(trade_result, context)

                # 6. Revise (самокоррекция)
                if reflection.get("requires_revision", False):
                    await self._revise(reflection)

                # Сохраняем результат для истории
                if trade_result:
                    self.last_trade_results.append(trade_result)
                    self.metrics_history.append({
                        "cycle": self.cycle_count,
                        "timestamp": datetime.utcnow().isoformat(),
                        "pnl": trade_result.get("pnl", 0),
                        "signal": trade_result.get("signal_type"),
                    })

                # Сохраняем состояние
                if self.cycle_count % 10 == 0:
                    self._save_state()

                # Проверка лимитов
                if self.max_cycles and self.cycle_count >= self.max_cycles:
                    logger.info(f"Достигнут лимит циклов ({self.max_cycles}). Остановка.")
                    break

                # Пауза перед следующим циклом
                await asyncio.sleep(self.config.get("cycle_interval_sec", 60))

            except Exception as e:
                logger.error(f"Критическая ошибка в цикле: {e}", exc_info=True)
                # Попытка самовосстановления
                await self._emergency_recovery(e)
                # Если восстановление не удалось — остановка
                if not self.running:
                    break

        logger.info("🛑 Оркестратор остановлен.")

    # ------------------------------------------------------------
    #  Фазы цикла
    # ------------------------------------------------------------

    async def _observe(self) -> Dict[str, Any]:
        """Сбор данных с бирж, новостей, ончейн."""
        # Здесь должен быть вызов MCP-серверов (CCXT, Alpha Vantage, Arkham)
        # Для примера — синтетические данные
        return {
            "underlying_price": 65000 + np.random.randn() * 200,
            "option_skew_25d": 0.12 + np.random.randn() * 0.02,
            "term_structure": 0.05 + np.random.randn() * 0.01,
            "volume_ratio": 1.0 + np.random.randn() * 0.2,
            "funding_rate": 0.0001 + np.random.randn() * 0.0005,
            "open_interest_change": 0.01 + np.random.randn() * 0.02,
            "order_book_imbalance": 0.02 + np.random.randn() * 0.03,
            "price_change_1h": 0.001 + np.random.randn() * 0.01,
            "iv_rank": 0.5 + np.random.randn() * 0.1,
        }

    async def _orient(self, market_data: Dict) -> Dict[str, Any]:
        """Построение контекста, извлечение знаний."""
        # Здесь используется RAG и граф контекста
        # Для демонстрации — просто возвращаем рыночные данные
        return {"market": market_data}

    async def _decide(self, market_data: Dict, context: Dict) -> Dict[str, Any]:
        """Принятие решения: использовать классический или квантовый детектор."""
        # 1. Классический сигнал
        classical_signal, classical_metrics = self.classical_detector.detect(market_data)

        # 2. Квантовый сигнал (если включён)
        quantum_signal = False
        quantum_metrics = {}
        if self.quantum_detector is not None:
            q_score, q_metrics = self.quantum_detector.detect(market_data)
            quantum_signal = q_score < self.config.get("quantum_threshold", -0.5)
            quantum_metrics = q_metrics

        # 3. Комбинированное решение (можно сделать более сложную логику)
        # Например: если оба сигнала True → увеличить позицию, если только один → уменьшить
        signal_type = "none"
        confidence = 0.0

        if classical_signal and quantum_signal:
            signal_type = "long_strangle"
            confidence = 0.9  # высокая уверенность
        elif classical_signal and not quantum_signal:
            signal_type = "long_strangle"
            confidence = 0.6  # средняя
        elif not classical_signal and quantum_signal:
            signal_type = "long_strangle"
            confidence = 0.7  # квант перевесил
        else:
            signal_type = "none"
            confidence = 0.0

        # 4. Проверка Vibe Check (не даёт переоптимизировать)
        vibe_ok = self.vibe_check.check(signal_type, confidence)
        if not vibe_ok:
            logger.warning("Vibe Check отклонил сигнал (возможное перепроектирование).")
            signal_type = "none"
            confidence = 0.0

        return {
            "signal_type": signal_type,
            "confidence": confidence,
            "classical": classical_metrics,
            "quantum": quantum_metrics,
            "timestamp": datetime.utcnow().isoformat(),
        }

    async def _act(self, decision: Dict, market_data: Dict) -> Optional[Dict]:
        """Исполнение решения через Executor / Hedger / PositionManager."""
        if decision["signal_type"] == "none":
            logger.info("Сигнал отсутствует, пропускаем исполнение.")
            return None

        # 1. Строим позицию (Long Strangle)
        position = self.executor.build_position(
            underlying=market_data["underlying_price"],
            skew=market_data["option_skew_25d"],
            confidence=decision["confidence"]
        )

        # 2. Хеджируем дельту
        hedge_order = self.hedger.hedge(position, market_data)

        # 3. Управляем рисками
        risk_ok = self.position_manager.validate(position, hedge_order)
        if not risk_ok:
            logger.warning("Позиция не прошла риск-контроль. Отмена.")
            return None

        # 4. Исполняем (в dry-run только логируем)
        if self.config.get("dry_run", True):
            logger.info(f"DRY-RUN: Открыта позиция {position}")
            trade_result = {
                "status": "simulated",
                "signal_type": decision["signal_type"],
                "entry_price": market_data["underlying_price"],
                "size": position.get("size", 0.1),
                "pnl": 0.0,  # симуляция
                "timestamp": datetime.utcnow().isoformat(),
            }
        else:
            # Реальное исполнение через API биржи
            trade_result = self.executor.execute(position)
            # Добавляем хедж
            if hedge_order:
                self.hedger.execute_hedge(hedge_order)

        return trade_result

    async def _reflect(self, trade_result: Optional[Dict], context: Dict) -> Dict[str, Any]:
        """Анализ результатов, сбор метрик, запись в OdabNote."""
        if trade_result is None:
            return {"requires_revision": False}

        # 1. Записываем в OdabNote паттерн
        self.odab_note.record(
            event_type="trade",
            data=trade_result,
            context=context
        )

        # 2. Вычисляем эффективность (если есть PnL)
        pnl = trade_result.get("pnl", 0)
        signal_type = trade_result.get("signal_type", "unknown")

        # 3. Если убыточная серия — триггер для рефлексии
        recent_losses = [r.get("pnl", 0) for r in self.last_trade_results[-10:] if r.get("pnl", 0) < 0]
        if len(recent_losses) >= 3:
            logger.warning(f"Обнаружено {len(recent_losses)} убыточных сделок подряд. Запуск рефлексии.")
            reflection_result = self.reflection_loop.run(
                history=self.last_trade_results[-20:],
                detector=self.classical_detector,
                quantum_detector=self.quantum_detector
            )
            return {
                "requires_revision": True,
                "reflection_data": reflection_result,
                "reason": "consistent_losses"
            }

        # 4. Квантовая рефлексия (если включена)
        if self.quantum_reflection is not None and self.quantum_detector is not None:
            quantum_advice = self.quantum_reflection.reflect(self.last_trade_results[-5:])
            if quantum_advice.get("actions"):
                logger.info(f"Квантовая рефлексия рекомендует: {quantum_advice['actions']}")
                return {
                    "requires_revision": True,
                    "reflection_data": quantum_advice,
                    "reason": "quantum_advice"
                }

        return {"requires_revision": False}

    async def _revise(self, reflection: Dict) -> None:
        """Автономное исправление: изменение параметров, кода, стратегий."""
        logger.info("🔧 Запуск автономной коррекции...")

        reason = reflection.get("reason", "unknown")
        data = reflection.get("reflection_data", {})

        if reason == "consistent_losses":
            # Уменьшаем риск, пересчитываем пороги
            new_threshold = self.classical_detector.threshold - 0.1  # делаем более чувствительным
            self.classical_detector.set_threshold(new_threshold)
            if self.quantum_detector:
                self.quantum_detector.set_threshold(new_threshold - 0.05)
            logger.info(f"Порог скорректирован до {new_threshold:.2f}")

            # Также можно уменьшить размер позиции
            self.executor.position_scale *= 0.8
            logger.info(f"Размер позиции уменьшен до {self.executor.position_scale:.2f}")

        elif reason == "quantum_advice":
            actions = data.get("actions", [])
            for action in actions:
                if "уменьшить n_qubits" in action:
                    # меняем конфиг и переобучаем квантовый детектор
                    self._reconfigure_quantum(n_qubits_delta=-2)
                elif "увеличить reps" in action:
                    self._reconfigure_quantum(reps_delta=+1)
                elif "сменить feature_map" in action:
                    self._reconfigure_quantum(feature_map="dense")

        # Записываем действие в OdabNote
        self.odab_note.record(
            event_type="self_revision",
            data={"reason": reason, "actions": actions if reason == "quantum_advice" else []},
            context={"cycle": self.cycle_count}
        )

        # Перезапускаем обученные модели с новыми параметрами
        # (в реальной жизни — асинхронно, без остановки основного цикла)

    def _reconfigure_quantum(self, n_qubits_delta=0, reps_delta=0, feature_map=None):
        """Переконфигурирует квантовый детектор и переобучает его."""
        if self.quantum_detector is None:
            return
        # Здесь должна быть логика изменения параметров и повторного обучения
        logger.info("Квантовая реконфигурация выполнена.")

    async def _emergency_recovery(self, error: Exception):
        """Экстренное восстановление при критической ошибке."""
        logger.critical(f"Аварийное восстановление: {error}")
        # Попробовать перезапустить компоненты
        try:
            self._init_components()
            logger.info("Компоненты переинициализированы.")
        except Exception as e:
            logger.error(f"Не удалось восстановиться: {e}")
            self.running = False


# ------------------------------------------------------------
#  Точка входа
# ------------------------------------------------------------

if __name__ == "__main__":
    import yaml
    import numpy as np   # для синтетики

    # Загрузка конфигурации
    with open("configs/orchestrator.yaml", 'r') as f:
        config = yaml.safe_load(f)

    # Создание и запуск оркестратора
    orchestrator = AriaOrchestrator(config)
    asyncio.run(orchestrator.run())
