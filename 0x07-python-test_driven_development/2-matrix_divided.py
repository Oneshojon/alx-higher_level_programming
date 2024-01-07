#!/usr/bin/python3
"""Function to divide all elements of a matrix."""


def matrix_divided(matrix, div):
    """
    Function to divide all elements of a matrix.

    Args:
        matrix (list): To be divided.
        div (number): devisor.

    Raises:
    TypeError: if matrix not list or div not a number.
    ZeroDivisionError: if div is zero.

    Returns:
    A new matrix.
    """
    message = "matrix must be a matrix (list of lists) of integers/floats"
    for row in matrix:
        if not row or not isinstance(row, list):
            raise TypeError(message)
        if not all(isinstance(i, (int, float)) for i in row):
            raise TypeError(message)
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = [[round(item / div, 2) for item in row] for row in matrix]
    return new_matrix
