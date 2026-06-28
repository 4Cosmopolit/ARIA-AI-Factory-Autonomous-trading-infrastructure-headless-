"""Быстрый тест квантового ядра."""

import numpy as np
from .kernel import QuantumKernel

def test_kernel_symmetry():
    kernel = QuantumKernel(n_qubits=2, feature_map="dense", reps=1, backend="default.qubit")
    X = np.random.randn(5, 2)
    K = kernel.gram_train(X)
    assert np.allclose(K, K.T), "Матрица Грама не симметрична"
    eigvals = np.linalg.eigvalsh(K)
    assert np.min(eigvals) >= -1e-6, "Матрица не PSD"
    print("✅ Тест пройден: симметричность и PSD.")

def test_kernel_concentration():
    kernel = QuantumKernel(n_qubits=3, feature_map="dense", reps=2, backend="default.qubit")
    X = np.random.randn(10, 3)
    K = kernel.gram_train(X)
    conc = kernel.kernel_concentration(K)
    print(f"Концентрация ядра: {conc:.3f}")
    assert 0.5 < conc < 10.0, "Концентрация вне ожидаемого диапазона"

if __name__ == "__main__":
    test_kernel_symmetry()
    test_kernel_concentration()
