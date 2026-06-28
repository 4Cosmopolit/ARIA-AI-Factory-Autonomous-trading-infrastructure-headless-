"""Фабрика устройств PennyLane."""

import pennylane as qml
from pennylane.devices import DefaultQubit

def make_device(n_qubits: int, backend: str = "lightning.qubit"):
    """Создаёт устройство PennyLane."""
    if backend.startswith("lightning"):
        try:
            # пытаемся импортировать lightning
            import pennylane_lightning  # noqa
            dev = qml.device(backend, wires=n_qubits)
        except ImportError:
            # fallback на default
            dev = qml.device("default.qubit", wires=n_qubits)
    elif backend == "default.qubit":
        dev = qml.device("default.qubit", wires=n_qubits)
    else:
        dev = qml.device(backend, wires=n_qubits)
    return dev
