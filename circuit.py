from typing import List
from .gates import Gate

class QuantumCircuit:
    """
    QuantumCircuit is responsible for creating and manipulating quantum circuits.
    """

    def __init__(self, num_qubits: int):
        self.num_qubits = num_qubits
        self.gates = []

    def add_gate(self, gate: Gate):
        if max(gate.qubits) >= self.num_qubits:
            raise ValueError("Gate qubits exceed the number of qubits in the circuit")
        self.gates.append(gate)

    def join_circuits(self, other_circuit):
        if self.num_qubits != other_circuit.num_qubits:
            raise ValueError("Circuits have a different number of qubits")
        self.gates.extend(other_circuit.gates)

    def measure(self, qubit: int, classical_bit: int = None) -> None:
        if classical_bit is None:
            classical_bit = qubit
        self.add_gate(Gate("measure", [qubit, classical_bit]))

    def __str__(self) -> str:
        circuit_str = f"QuantumCircuit with {self.num_qubits} qubits:\n"
        for gate in self.gates:
            circuit_str += f"  {gate}\n"
        return circuit_str

    def __repr__(self) -> str:
        return self.__str__()

