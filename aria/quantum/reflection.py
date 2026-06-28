"""Само-коррекция квантовых параметров (интеграция с OdabNote)."""

import numpy as np
from .kernel import QuantumKernel

class QuantumReflection:
    """
    Анализирует производительность квантового детектора и предлагает корректировки.
    """
    
    def __init__(self, engine, odab_note=None):
        self.engine = engine
        self.odab_note = odab_note
        self.history = []
    
    def reflect(self, trade_results: list):
        """
        trade_results: список словарей с полями 'signal', 'pnl', 'market_condition'
        """
        # Вычисляем метрики
        if len(trade_results) < 10:
            return {"action": "wait", "reason": "недостаточно данных"}
        
        # Квантовая предсказательная сила: корреляция между score и PnL
        scores = [r.get('quantum_score', 0) for r in trade_results]
        pnls = [r.get('pnl', 0) for r in trade_results]
        if len(scores) > 0 and np.std(scores) > 0:
            corr = np.corrcoef(scores, pnls)[0,1]
        else:
            corr = 0.0
        
        # Анализ концентрации ядра
        K = self.engine.K_train
        if K is not None:
            concentration = self.engine.kernel.kernel_concentration(K)
        else:
            concentration = 1.0
        
        # Решения
        actions = []
        if corr < 0.1:
            actions.append("уменьшить n_qubits на 2")
        if concentration > 5.0:
            actions.append("увеличить reps на 1 (слишком высокая концентрация)")
        if concentration < 1.2:
            actions.append("добавить энтанглмент (сменить feature_map на dense)")
        
        # Запись в OdabNote
        if self.odab_note and actions:
            self.odab_note.record(
                event_type="quantum_reflection",
                data={"corr": corr, "concentration": concentration, "actions": actions}
            )
        
        return {"actions": actions, "corr": corr, "concentration": concentration}
