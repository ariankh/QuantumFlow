class Qubit:
    """
    Represents a qubit in QuantumFlow.
    """

    def __init__(self, index: int):
        self.index = index
        self.state = None  # Replace None with the initial state of the qubit, typically |0> or a 2D vector representing the state.

    def __str__(self):
        return f"Qubit({self.index})"

    def __repr__(self):
        return self.__str__()

    def set_state(self, state):
        """
        Set the state of the qubit.
        Args:
            state: The new state of the qubit, typically represented as a 2D vector.
        """
        self.state = state

    def get_state(self):
        """
        Get the current state of the qubit.
        Returns:
            The current state of the qubit, typically represented as a 2D vector.
        """
        return self.state
