#!/usr/bin/python3
"""Defines a function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """Divide every element of a matrix by div, rounded to 2 decimals.

    Args:
        matrix (list of list of int/float): the matrix to divide
        div (int/float): the divisor

    Returns:
        list of list of float: a new matrix with divided elements
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix)):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    for row in matrix:
        if not all(isinstance(n, (int, float)) and not isinstance(n, bool)
                   for n in row):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)) or isinstance(div, bool):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(n / div, 2) for n in row] for row in matrix]
