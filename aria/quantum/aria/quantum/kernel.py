"""Квантовое ядро (fidelity kernel) для ARIA."""

import pennylane as qml
import numpy as np
from scipy.linalg import eigh
from .feature_maps import get_feature_map
from .device import make_device

class QuantumKernel:
    """Класс для вычисления fidelity kernel между двумя наборами данных."""
    
    def __init__(
        self,
        n_qubits: int,
        feature_map: str = "dense",
        reps: int = 2,
        backend: str = "lightning.qubit"
    ):
        self.n_qubits = n_qubits
        self.reps = reps
        self.feature_map = get_feature_map(feature_map, reps=reps)
        self.dev = make_device(n_qubits, backend)
        self._circuit = self._build_circuit()
    
    def _build_circuit(self):
        """Строит схему для вычисления fidelity: ⟨φ(x)|φ(y)⟩²."""
        @qml.qnode(self.dev)
        def kernel_circuit(x, y):
            # Кодируем x
            self.feature_map(x, wires=range(self.n_qubits))
            # Инвертируем кодирование y
            for i in range(self.n_qubits):
                qml.adjoint(self.feature_map)(y, wires=range(self.n_qubits))
            # Измеряем проекцию на |0⟩
            return qml.probs(wires=range(self.n_qubits))
        return kernel_circuit
    
    def gram_train(self, X_train):
        """
        Вычисляет матрицу Грама для обучающей выборки (N x N).
        Предполагается, что X_train уже нормализован и сжат до размерности n_qubits.
        """
        n = X_train.shape[0]
        K = np.zeros((n, n))
        for i in range(n):
            for j in range(i, n):
                probs = self._circuit(X_train[i], X_train[j])
                # fidelity = вероятность получить все нули
                f = probs[0]  # проекция на |0...0⟩
                # Симметризуем (учитываем численную асимметрию)
                f_sym = 0.5 * (f + self._circuit(X_train[j], X_train[i])[0])
                K[i, j] = K[j, i] = f_sym
        # Проверка PSD (небольшой регуляризатор)
        eigvals, _ = eigh(K)
        if np.min(eigvals) < 1e-6:
            K += 1e-6 * np.eye(n)
        return K
    
    def gram_test(self, X_train, X_test):
        """Вычисляет кросс-матрицу Грама (test x train)."""
        n_train = X_train.shape[0]
        n_test = X_test.shape[0]
        K = np.zeros((n_test, n_train))
        for i in range(n_test):
            for j in range(n_train):
                probs = self._circuit(X_test[i], X_train[j])
                K[i, j] = probs[0]  # проекция на |0...0⟩
        return K

    def kernel_concentration(self, K):
        """Мера концентрации ядра (диагональ vs офф-диагональ)."""
        diag = np.diag(K)
        off = K[np.triu_indices_from(K, k=1)]
        return np.mean(diag) / (np.mean(off) + 1e-8)
