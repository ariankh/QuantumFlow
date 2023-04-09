import numpy as np
from pyquil import Program, get_qc
from pyquil.gates import *
from ..circuit import QuantumCircuit
from .base_backend import Backend

from .base_backend import BaseBackend
# Other imports

class RigettiBackend(BaseBackend):  # Inherit from BaseBackend
    # Implementation

class RigettiBackend(Backend):
    """
    RigettiBackend interfaces with Rigetti's quantum hardware.
    """

    def __init__(self, device_name: str = 'Aspen-8'):
        self.device_name = device_name
        self.backend = get_qc(f'{device_name}_qvm')

    @staticmethod
    def _convert_to_pyquil_program(qf_circuit: QuantumCircuit) -> Program:
        pyquil_program = Program()
        for gate in qf_circuit.gates:
            pyquil_gate = globals()[gate.name.upper()]
            pyquil_program.inst(pyquil_gate(*gate.qubits))
        pyquil_program.measure_all()
        return pyquil_program

    def run(self, circuit: QuantumCircuit, shots: int = 1024):
        pyquil_program = self._convert_to_pyquil_program(circuit)
        executable = self.backend.compile(pyquil_program)
        result = self.backend.run(executable, shots=shots)
        return result.tolist()

    def get_backend_info(self):
        return {
            'name': 'RigettiBackend',
            'device_name': self.device_name,
            'version': '0.1.0',
            'provider': 'Rigetti Computing',
            'supported_gates': ['i', 'x', 'y', 'z', 'h', 's', 't', 'rx', 'ry', 'rz', 'cx', 'cz', 'swap', 'ccx']
        }
