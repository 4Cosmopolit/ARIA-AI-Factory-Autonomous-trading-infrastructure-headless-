"""Основной движок квантового детектора аномалий."""

import numpy as np
import yaml
import logging
from pathlib import Path
from typing import Dict, Any

from .kernel import QuantumKernel
from .encoder import PCAEncoder, AutoencoderEncoder
from .scorer import QuantumSVM
from .adapter import FinancialDomainAdapter

logger = logging.getLogger(__name__)

class AnomalyEngine:
    """
    Интегрирует энкодер, квантовое ядро и скорер.
    Предоставляет интерфейс для обучения и прогнозирования.
    """
    
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.quantum_cfg = config['quantum']
        self.encoder_cfg = config['encoder']
        self.domain_cfg = config['domain']
        
        self.n_qubits = self.quantum_cfg['n_qubits']
        self.feature_map = self.quantum_cfg['feature_map']
        self.reps = self.quantum_cfg['reps']
        self.backend = self.quantum_cfg['backend']
        self.nu = self.quantum_cfg['nu']
        
        # Инициализация компонентов
        self.kernel = QuantumKernel(
            n_qubits=self.n_qubits,
            feature_map=self.feature_map,
            reps=self.reps,
            backend=self.backend
        )
        
        if self.encoder_cfg['kind'] == 'pca':
            self.encoder = PCAEncoder(
                latent_dim=self.n_qubits,
                standardize=self.encoder_cfg.get('standardize', True)
            )
        elif self.encoder_cfg['kind'] == 'ae':
            self.encoder = AutoencoderEncoder(
                input_dim=... # будет установлено при fit
            )
        else:
            raise ValueError("Неизвестный тип энкодера")
        
        self.scorer = QuantumSVM(nu=self.nu)
        self.adapter = FinancialDomainAdapter(
            lookback=self.domain_cfg.get('lookback', 30),
            n_qubits=self.n_qubits
        )
        
        self.is_fitted = False
        self.X_train_encoded = None
        self.K_train = None
    
    def fit(self, X: np.ndarray):
        """
        Обучение на нормальных данных (X — признаки).
        """
        # Кодирование
        self.encoder.fit(X)
        Z_train = self.encoder.transform(X)
        self.X_train_encoded = Z_train
        
        # Квантовое ядро
        self.K_train = self.kernel.gram_train(Z_train)
        
        # Scorer
        self.scorer.fit(self.K_train)
        self.is_fitted = True
        logger.info("Квантовый детектор обучен на %d образцах", X.shape[0])
        return self
    
    def predict(self, X: np.ndarray) -> np.ndarray:
        """
        Возвращает метки: 1=normal, -1=anomaly.
        """
        if not self.is_fitted:
            raise RuntimeError("Детектор не обучен.")
        
        Z_test = self.encoder.transform(X)
        K_test = self.kernel.gram_test(self.X_train_encoded, Z_test)
        return self.scorer.predict(K_test)
    
    def score_samples(self, X: np.ndarray) -> np.ndarray:
        """Возвращает anomaly scores (чем ниже, тем более аномально)."""
        if not self.is_fitted:
            raise RuntimeError("Детектор не обучен.")
        Z_test = self.encoder.transform(X)
        K_test = self.kernel.gram_test(self.X_train_encoded, Z_test)
        return self.scorer.score(K_test)
    
    @classmethod
    def from_config_file(cls, path: str):
        with open(path, 'r') as f:
            config = yaml.safe_load(f)
        return cls(config)
    
    def evaluate(self, X_test, y_test):
        """Вычисляет AUC ROC и другие метрики."""
        from sklearn.metrics import roc_auc_score, accuracy_score
        y_pred = self.predict(X_test)
        scores = self.score_samples(X_test)
        # Для OneClassSVM: метки 1/-1, преобразуем в вероятности для AUC
        # Используем scores напрямую как меру аномальности
        auc = roc_auc_score((y_test == -1).astype(int), -scores)
        acc = accuracy_score(y_test, y_pred)
        return {'auc': auc, 'accuracy': acc}
