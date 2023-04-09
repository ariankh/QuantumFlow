import numpy as np
from typing import Tuple


def is_unitary(matrix: np.ndarray, tolerance: float = 1e-9) -> bool:
    """
    Checks if a given matrix is unitary.

    Args:
        matrix: The input numpy array representing the matrix.
        tolerance: The tolerance for checking if the matrix is unitary (default: 1e-9).

    Returns:
        True if the matrix is unitary, False otherwise.
    """
    identity_matrix = np.eye(matrix.shape[0])
    product = np.dot(matrix, np.conj(matrix.T))
    return np.allclose(product, identity_matrix, atol=tolerance)


def is_hermitian(matrix: np.ndarray, tolerance: float = 1e-9) -> bool:
    """
    Checks if a given matrix is Hermitian.

    Args:
        matrix: The input numpy array representing the matrix.
        tolerance: The tolerance for checking if the matrix is Hermitian (default: 1e-9).

    Returns:
        True if the matrix is Hermitian, False otherwise.
    """
    return np.allclose(matrix, np.conj(matrix.T), atol=tolerance)


def kronecker_product(matrix1: np.ndarray, matrix2: np.ndarray) -> np.ndarray:
    """
    Computes the Kronecker product of two matrices.

    Args:
        matrix1: The first input numpy array representing a matrix.
        matrix2: The second input numpy array representing a matrix.

    Returns:
        A numpy array representing the Kronecker product of the input matrices.
    """
    return np.kron(matrix1, matrix2)


def pauli_matrices() -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Returns the Pauli matrices X, Y, and Z as numpy arrays.

    Returns:
        A tuple containing the X, Y, and Z Pauli matrices as numpy arrays.
    """
    X = np.array([[0, 1], [1, 0]], dtype=complex)
    Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
    Z = np.array([[1, 0], [0, -1]], dtype=complex)

    return X, Y, Z
