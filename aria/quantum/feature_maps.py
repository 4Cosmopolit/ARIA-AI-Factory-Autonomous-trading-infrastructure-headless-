"""Feature maps для PennyLane — повторяемые слои с энтанглментом."""

import pennylane as qml
import numpy as np

def get_feature_map(name: str, reps: int = 2):
    """Возвращает функцию feature map по имени."""
    registry = {
        "dense": _dense_feature_map,
        "dense_no_ent": _dense_no_entanglement,
        "angle": _angle_feature_map,
        "iqp": _iqp_feature_map,
    }
    if name not in registry:
        raise ValueError(f"Неизвестный feature map: {name}. Доступны: {list(registry.keys())}")
    
    def feature_map(x, wires):
        registry[name](x, wires, reps)
    return feature_map

def _dense_feature_map(x, wires, reps):
    """Dense feature map из статьи: RY + CNOT entanglement."""
    n_qubits = len(wires)
    for _ in range(reps):
        for i, wire in enumerate(wires):
            qml.RY(x[i % len(x)], wires=wire)
        # Энтанглмент: CNOT между соседними кубитами с циклическим замыканием
        for i in range(n_qubits):
            qml.CNOT(wires=[wires[i], wires[(i + 1) % n_qubits]])

def _dense_no_entanglement(x, wires, reps):
    """Без энтанглмента — для бенчмаркинга."""
    n_qubits = len(wires)
    for _ in range(reps):
        for i, wire in enumerate(wires):
            qml.RY(x[i % len(x)], wires=wire)
        # Нет CNOT

def _angle_feature_map(x, wires, reps):
    """Angle encoding (простой вариант)."""
    for i, wire in enumerate(wires):
        qml.RX(x[i % len(x)], wires=wire)

def _iqp_feature_map(x, wires, reps):
    """IQP-style feature map (из PennyLane примеров)."""
    n_qubits = len(wires)
    for _ in range(reps):
        for i, wire in enumerate(wires):
            qml.Hadamard(wires=wire)
            qml.RZ(x[i % len(x)], wires=wire)
        for i in range(n_qubits):
            qml.CNOT(wires=[wires[i], wires[(i + 1) % n_qubits]])
