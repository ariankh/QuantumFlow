from .circuit import QuantumCircuit
from .gates import *
from .qubit import Qubit
from .qubit_array import QubitArray
from .register import QuantumRegister
from .compiler import compile_circuit
from .resource_estimation import gate_count, qubit_count, circuit_depth
from .simulator import QuantumSimulator
from .transformations import *
from .backends import *

__version__ = '0.1.0'
__all__ = [
    'QuantumCircuit',
    'Qubit',
    'QubitArray',
    'QuantumRegister',
    'compile_circuit',
    'gate_count',
    'qubit_count',
    'circuit_depth',
    'QuantumSimulator',
    '__version__'
]
