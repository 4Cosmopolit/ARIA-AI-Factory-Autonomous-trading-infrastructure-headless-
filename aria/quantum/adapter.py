"""Адаптер для финансовых данных (Bybit / Alpha Vantage)."""

import numpy as np
import pandas as pd
from typing import Tuple, Dict, Any

class FinancialDomainAdapter:
    """
    Адаптирует рыночные данные для квантового детектора.
    Выход: признаки (returns, volatility, volume, skew, funding, OI, etc.)
    """
    
    def __init__(self, lookback: int = 30, n_qubits: int = 8):
        self.lookback = lookback
        self.n_qubits = n_qubits
        self.feature_names = None
    
    def ingest(self, ohlcv: pd.DataFrame, fund_rate: pd.Series = None, oi: pd.Series = None,
               option_skew: pd.Series = None) -> np.ndarray:
        """
        ohlcv: DataFrame с колонками ['open','high','low','close','volume'].
        fund_rate: ставка финансирования (опционально).
        oi: открытый интерес (опционально).
        option_skew: опционный skew (опционально).
        
        Возвращает: X (n_samples, n_features) — подготовленные признаки.
        """
        # 1. Базовые признаки
        returns = ohlcv['close'].pct_change().fillna(0)
        log_ret = np.log(ohlcv['close'] / ohlcv['close'].shift(1)).fillna(0)
        
        # Волатильность за lookback
        vol = log_ret.rolling(self.lookback).std().fillna(method='bfill')
        
        # Объёмный импульс
        volume_ratio = ohlcv['volume'] / ohlcv['volume'].rolling(self.lookback).mean().fillna(1)
        
        # 2. Расширенные признаки (если есть)
        features = pd.DataFrame({
            'ret_1h': log_ret,
            'ret_4h': log_ret.rolling(4).sum(),
            'vol_1h': vol,
            'vol_4h': log_ret.rolling(4).std().fillna(0),
            'volume_ratio': volume_ratio,
            'high_low_ratio': (ohlcv['high'] - ohlcv['low']) / (ohlcv['close'] + 1e-8),
            'close_open': (ohlcv['close'] - ohlcv['open']) / (ohlcv['open'] + 1e-8),
        })
        
        # Добавляем funding rate если есть
        if fund_rate is not None:
            features['funding'] = fund_rate
        
        # Добавляем OI изменение если есть
        if oi is not None:
            features['oi_change'] = oi.pct_change().fillna(0)
        
        # Добавляем skew если есть
        if option_skew is not None:
            features['skew'] = option_skew
        
        # Убираем NaN (заполняем нулями)
        X = features.fillna(0).values
        self.feature_names = features.columns.tolist()
        return X.astype(np.float32)
    
    def split(self, X: np.ndarray, anomaly_ratio: float = 0.05) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
        """
        Разделяет на train (норма) и test (норма + аномалии).
        Аномалии — случайные подмножества (имитация кризисных событий).
        """
        n = X.shape[0]
        # Train: первые 70% или фиксированное количество
        train_size = max(500, int(0.7 * n))
        X_train = X[:train_size]
        X_test = X[train_size:]
        
        # Искусственные аномалии: добавляем шум с большой амплитудой
        n_test = X_test.shape[0]
        n_anomalies = int(anomaly_ratio * n_test)
        if n_anomalies > 0:
            anomaly_idx = np.random.choice(n_test, n_anomalies, replace=False)
            X_test_anom = X_test[anomaly_idx].copy()
            # Усиленный шум
            noise = np.random.normal(0, 5, size=X_test_anom.shape)
            X_test_anom += noise
            X_test[anomaly_idx] = X_test_anom
        
        # y: 1=normal, -1=anomaly
        y_train = np.ones(train_size)
        y_test = np.ones(n_test)
        if n_anomalies > 0:
            y_test[anomaly_idx] = -1
        
        return X_train, y_train, X_test, y_test
