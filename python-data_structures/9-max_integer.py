#!/usr/bin/python3
"""Module that finds the biggest integer of a list."""


def max_integer(my_list=[]):
    """Return the biggest integer of a list, or None if the list is empty."""
    if len(my_list) == 0:
        return None
    biggest = my_list[0]
    for integer in my_list:
        if integer > biggest:
            biggest = integer
    return biggest
