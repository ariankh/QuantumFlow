from .qubit_array import QubitArray


class QuantumRegister:
    """
    Represents a quantum register for organizing qubits within a quantum circuit.
    """

    def __init__(self, num_qubits: int, name: str = None):
        self.qubit_array = QubitArray(num_qubits)
        self.name = name if name else f"qreg{hash(self)}"

    def __getitem__(self, index):
        return self.qubit_array[index]

    def __setitem__(self, index, value):
        self.qubit_array[index] = value

    def __len__(self):
        return len(self.qubit_array)

    def __str__(self):
        return f"QuantumRegister(name={self.name}, qubits={self.qubit_array})"

    def __repr__(self):
        return self.__str__()

    def get_qubit(self, index: int):
        """
        Get the Qubit at the specified index in the QuantumRegister.
        Args:
            index: The index of the qubit to retrieve.
        Returns:
            The Qubit at the specified index.
        """
        return self.qubit_array.get_qubit(index)

    def set_qubit(self, index: int, qubit):
        """
        Set the Qubit at the specified index in the QuantumRegister.
        Args:
            index: The index of the qubit to set.
            qubit: The new Qubit to replace the existing one.
        """
        self.qubit_array.set_qubit(index, qubit)
