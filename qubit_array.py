from .qubit import Qubit


class QubitArray:
    """
    Represents an array of qubits in QuantumFlow.
    """

    def __init__(self, num_qubits: int):
        self.qubits = [Qubit(i) for i in range(num_qubits)]

    def __getitem__(self, index):
        return self.qubits[index]

    def __setitem__(self, index, value):
        self.qubits[index] = value

    def __len__(self):
        return len(self.qubits)

    def __str__(self):
        return f"QubitArray([{', '.join(str(qubit) for qubit in self.qubits)}])"

    def __repr__(self):
        return self.__str__()

    def get_qubit(self, index: int) -> Qubit:
        """
        Get the Qubit at the specified index in the QubitArray.
        Args:
            index: The index of the qubit to retrieve.
        Returns:
            The Qubit at the specified index.
        """
        return self.qubits[index]

    def set_qubit(self, index: int, qubit: Qubit):
        """
        Set the Qubit at the specified index in the QubitArray.
        Args:
            index: The index of the qubit to set.
            qubit: The new Qubit to replace the existing one.
        """
        self.qubits[index] = qubit

    def apply_gate(self, gate, *qubit_indices):
        """
        Apply a quantum gate to the specified qubits in the QubitArray.
        Args:
            gate: The quantum gate to apply.
            qubit_indices: The indices of the qubits to apply the gate to.
        """
        # Implement the logic for applying the gate to the qubits in the array.
