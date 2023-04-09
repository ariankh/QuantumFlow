import numpy as np
from .circuit import QuantumCircuit
from .backends.base_backend import Backend
from .qubit import Qubit
from .qubit_array import QubitArray


class Simulator(Backend):
    """
    Implements a noise-free quantum simulator for running QuantumFlow programs.
    """

    def __init__(self, name: str = "Simulator"):
        super().__init__(name)

    def run(self, circuit: QuantumCircuit, shots: int = 1, **kwargs) -> dict:
        """
        Executes the given quantum circuit using the noise-free simulator.

        Args:
            circuit: The QuantumCircuit to be executed.
            shots: The number of times to execute the circuit (default: 1).
            **kwargs: Additional keyword arguments for execution.

        Returns:
            A dictionary containing the results, including the execution counts.
        """
        state = self.initialize_state(circuit.qubits)
        state = self.simulate(circuit, state)
        counts = self.measure(state, circuit.qubits, shots)

        return {"counts": counts}

    def initialize_state(self, qubits: QubitArray) -> np.ndarray:
        """
        Initializes the state vector for the given qubits.

        Args:
            qubits: The QubitArray for which to initialize the state vector.

        Returns:
            The initialized state vector as a NumPy array.
        """
        state = np.zeros(2 ** len(qubits), dtype=complex)
        state[0] = 1
        return state

    def simulate(self, circuit: QuantumCircuit, state: np.ndarray) -> np.ndarray:
        """
        Simulates the given quantum circuit on the provided state vector.

        Args:
            circuit: The QuantumCircuit to be simulated.
            state: The state vector as a NumPy array.

        Returns:
            The resulting state vector after simulation.
        """
        for operation in circuit.operations:
            state = operation.apply(state)
        return state

    def measure(self, state: np.ndarray, qubits: QubitArray, shots: int) -> dict:
        """
        Measures the given state vector for the specified number of shots.

        Args:
            state: The state vector as a NumPy array.
            qubits: The QubitArray to measure.
            shots: The number of times to execute the measurement.

        Returns:
            A dictionary containing the measurement counts.
        """
        probabilities = np.abs(state) ** 2
        outcomes = range(2 ** len(qubits))
        counts = np.random.choice(outcomes, p=probabilities, size=shots)
        result = {format(outcome, f"0{len(qubits)}b"): 0 for outcome in outcomes}

        for count in counts:
            result[format(count, f"0{len(qubits)}b")] += 1

        return result
