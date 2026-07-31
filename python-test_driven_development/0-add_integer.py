#!/usr/bin/python3
"""Defines a function that adds two integers.
"""


def add_integer(a, b=98):
    """Add two integers or floats together.

    a and b are cast to int before the addition. Raises TypeError if
    either a or b is not an int or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
