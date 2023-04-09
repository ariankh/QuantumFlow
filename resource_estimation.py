from .circuit import QuantumCircuit
from collections import Counter


def gate_counts(circuit: QuantumCircuit) -> Counter:
    """
    Counts the number of each type of gate used in the quantum circuit.

    Args:
        circuit: The QuantumCircuit for which to count gate types.

    Returns:
        A Counter object containing the counts of each gate type.
    """
    gate_counter = Counter()
    for operation in circuit.operations:
        gate_counter[operation.gate.__class__.__name__] += 1
    return gate_counter


def qubit_count(circuit: QuantumCircuit) -> int:
    """
    Counts the number of qubits used in the quantum circuit.

    Args:
        circuit: The QuantumCircuit for which to count qubits.

    Returns:
        The number of qubits used in the circuit.
    """
    return len(circuit.qubits)


def depth(circuit: QuantumCircuit) -> int:
    """
    Computes the depth of the quantum circuit.

    Args:
        circuit: The QuantumCircuit for which to compute the depth.

    Returns:
        The depth of the quantum circuit.
    """
    return circuit.depth()


def width(circuit: QuantumCircuit) -> int:
    """
    Computes the width of the quantum circuit.

    Args:
        circuit: The QuantumCircuit for which to compute the width.

    Returns:
        The width of the quantum circuit.
    """
    return len(circuit.qubits)
