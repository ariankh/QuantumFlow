from qiskit import QuantumCircuit as QiskitCircuit, execute, Aer
from qiskit.providers.aer import QasmSimulator
from ..circuit import QuantumCircuit
from .base_backend import Backend

class QiskitBackend(Backend):
    """
    QiskitBackend interfaces with IBM's Qiskit.
    """

    def __init__(self, simulator: bool = True):
        self.simulator = simulator
        if simulator:
            self.backend = QasmSimulator()
        else:
            self.backend = Aer.get_backend('ibmq_qasm_simulator')

    @staticmethod
    def _convert_to_qiskit_circuit(qf_circuit: QuantumCircuit) -> QiskitCircuit:
        qiskit_circuit = QiskitCircuit(qf_circuit.num_qubits)
        for gate in qf_circuit.gates:
            qiskit_gate = getattr(qiskit_circuit, gate.name)
            qiskit_gate(*gate.qubits)
        qiskit_circuit.measure_all()
        return qiskit_circuit

    def run(self, circuit: QuantumCircuit, shots: int = 1024):
        qiskit_circuit = self._convert_to_qiskit_circuit(circuit)
        job = execute(qiskit_circuit, self.backend, shots=shots)
        result = job.result()
        return result.get_counts(qiskit_circuit)

    def get_backend_info(self):
        return {
            'name': 'QiskitBackend',
            'simulator': self.simulator,
            'version': '0.1.0',
            'provider': 'IBM Qiskit',
            'supported_gates': ['x', 'y', 'z', 'h', 's', 't', 'rx', 'ry', 'rz', 'cx', 'cz', 'swap', 'ccx']
        }
