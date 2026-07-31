#!/usr/bin/python3
"""Defines a function that prints a square of '#' characters.
"""


def print_square(size):
    """Print a square with the character '#'.

    Args:
        size (int): the length of the square's sides
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
