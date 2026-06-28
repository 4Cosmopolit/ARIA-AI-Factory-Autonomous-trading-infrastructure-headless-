"""Квантовое ядро для ARIA — anomaly detection на основе PennyLane."""

from .kernel import QuantumKernel
from .feature_maps import get_feature_map
from .device import make_device
from .encoder import PCAEncoder, AutoencoderEncoder
from .scorer import QuantumSVM, QuantumKMeans
from .adapter import FinancialDomainAdapter
from .engine import AnomalyEngine
from .reflection import QuantumReflection

__all__ = [
    "QuantumKernel",
    "get_feature_map",
    "make_device",
    "PCAEncoder",
    "AutoencoderEncoder",
    "QuantumSVM",
    "QuantumKMeans",
    "FinancialDomainAdapter",
    "AnomalyEngine",
    "QuantumReflection",
]
