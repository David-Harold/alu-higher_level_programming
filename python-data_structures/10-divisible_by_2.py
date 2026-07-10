#!/usr/bin/python3
"""Module that finds all multiples of 2 in a list."""


def divisible_by_2(my_list=[]):
    """Return a new list of the same size, with True/False depending
    on whether the integer at the same position is a multiple of 2."""
    result = []
    for integer in my_list:
        result.append(integer % 2 == 0)
    return result
