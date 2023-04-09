from .circuit import QuantumCircuit
from typing import Callable, List

class QuantumFlowCompiler:
    """
    QuantumFlowCompiler optimizes quantum circuits.
    """

    def __init__(self, optimizations: List[Callable[[QuantumCircuit], None]] = None):
        self.optimizations = optimizations or []

    def add_optimization(self, optimization: Callable[[QuantumCircuit], None]) -> None:
        self.optimizations.append(optimization)

    def compile(self, circuit: QuantumCircuit) -> QuantumCircuit:
        optimized_circuit = circuit.copy()
        for optimization in self.optimizations:
            optimization(optimized_circuit)
        return optimized_circuit
