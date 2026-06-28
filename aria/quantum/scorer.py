"""Скореры на основе квантовых ядер (QSVM, Qk-means)."""

import numpy as np
from sklearn.svm import OneClassSVM
from sklearn.cluster import KMeans

class QuantumSVM:
    """
    One-class SVM с предварительно вычисленным квантовым ядром.
    Используется для обнаружения аномалий.
    """
    
    def __init__(self, nu: float = 0.1, gamma: str = "auto"):
        self.nu = nu
        self.gamma = gamma
        self.svm = None
        self.is_fitted = False
    
    def fit(self, K_train):
        """
        K_train: матрица Грама (n_train, n_train) — уже квантовое ядро.
        """
        self.svm = OneClassSVM(kernel="precomputed", nu=self.nu, gamma=self.gamma)
        self.svm.fit(K_train)
        self.is_fitted = True
        return self
    
    def score(self, K_test_train):
        """
        K_test_train: кросс-ядро (n_test, n_train).
        Возвращает anomaly scores (отрицательные = аномалии).
        """
        if not self.is_fitted:
            raise RuntimeError("Модель не обучена.")
        return self.svm.score_samples(K_test_train)
    
    def predict(self, K_test_train):
        if not self.is_fitted:
            raise RuntimeError("Модель не обучена.")
        return self.svm.predict(K_test_train)

class QuantumKMeans:
    """K-means с квантовым ядром (kernel k-means)."""
    
    def __init__(self, n_clusters: int = 2, max_iter: int = 100):
        self.n_clusters = n_clusters
        self.max_iter = max_iter
        self.centers = None
        self.is_fitted = False
    
    def fit(self, K_train):
        """K_train: (n_train, n_train) — квантовая матрица Грама."""
        from sklearn.cluster import SpectralClustering
        # Используем спектральную кластеризацию на ядре
        sc = SpectralClustering(n_clusters=self.n_clusters, affinity='precomputed', random_state=42)
        labels = sc.fit_predict(K_train)
        self.centers = labels
        self.is_fitted = True
        return self
    
    def predict(self, K_test_train):
        """K_test_train: (n_test, n_train) — кросс-ядро."""
        # Простая эвристика: ближайший центр по среднему сходству
        n_test = K_test_train.shape[0]
        labels = np.zeros(n_test)
        for i in range(n_test):
            similarities = K_test_train[i, :]
            # Суммируем сходство с каждым кластером
            cluster_scores = []
            for c in range(self.n_clusters):
                mask = (self.centers == c)
                if np.sum(mask) > 0:
                    cluster_scores.append(np.mean(similarities[mask]))
                else:
                    cluster_scores.append(-np.inf)
            labels[i] = np.argmax(cluster_scores)
        return labels
