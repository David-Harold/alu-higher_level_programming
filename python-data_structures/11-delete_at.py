#!/usr/bin/python3
"""Module that deletes the item at a specific position in a list."""


def delete_at(my_list=[], idx=0):
    """Return a new list with the item at idx removed. If idx is
    negative or out of range, return the list unchanged."""
    if idx < 0 or idx >= len(my_list):
        return my_list
    return my_list[:idx] + my_list[idx + 1:]
