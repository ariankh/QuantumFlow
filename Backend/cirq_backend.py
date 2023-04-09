import cirq
from ..circuit import QuantumCircuit
from .base_backend import Backend

class CirqBackend(Backend):
    """
    CirqBackend interfaces with Google's Cirq.
    """

    def __init__(self, simulator: bool = True):
        self.simulator = simulator
        if simulator:
            self.backend = cirq.Simulator()

    @staticmethod
    def _convert_to_cirq_circuit(qf_circuit: QuantumCircuit) -> cirq.Circuit:
        cirq_circuit = cirq.Circuit()
        for gate in qf_circuit.gates:
            cirq_gate = getattr(cirq, gate.name.upper())
            cirq_circuit.append(cirq_gate(*gate.qubits))
        cirq_circuit.append(cirq.measure(*qf_circuit.qubits, key='result'))
        return cirq_circuit

    def run(self, circuit: QuantumCircuit, shots: int = 1024):
        cirq_circuit = self._convert_to_cirq_circuit(circuit)
        result = self.backend.run(cirq_circuit, repetitions=shots)
        return result.measurements['result'].tolist()

    def get_backend_info(self):
        return {
            'name': 'CirqBackend',
            'simulator': self.simulator,
            'version': '0.1.0',
            'provider': 'Google Cirq',
            'supported_gates': ['x', 'y', 'z', 'h', 's', 't', 'rx', 'ry', 'rz', 'cx', 'cz', 'swap', 'ccx']
        }
