"""
Hunter 6.0 — модуль опционного арбитража волатильности.

Содержит:
- AdaptiveSkewDetector — основной детектор перекоса (Isolation Forest + онлайн-обучение)
- QuantumSkewDetector — альтернативный квантовый детектор (PennyLane + QSVM)
- Executor — построение позиции Long Strangle
- Hedger — дельта-хеджирование фьючерсами
- PositionManager — управление рисками (TP/SL, Theta Shield, трейлинг)
"""

from .adaptive_skew_detector import AdaptiveSkewDetector
from .executor import Executor
from .hedger import Hedger
from .position_manager import PositionManager
from .quantum_detector import QuantumSkewDetector   # <-- новый импорт

__all__ = [
    "AdaptiveSkewDetector",
    "QuantumSkewDetector",
    "Executor",
    "Hedger",
    "PositionManager",
]
from .quantum_detector import QuantumSkewDetector
