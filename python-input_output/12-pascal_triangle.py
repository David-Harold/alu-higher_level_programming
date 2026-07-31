#!/usr/bin/python3
"""Defines a pascal_triangle function."""


def pascal_triangle(n):
    """Return a list of lists of integers representing Pascal's triangle.

    Args:
        n (int): The number of rows to generate.

    Returns:
        list: A list of n rows of Pascal's triangle, or an empty list
        if n is less than or equal to 0.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        prev_row = triangle[-1]
        row = [1]
        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])
        row.append(1)
        triangle.append(row)
    return triangle
