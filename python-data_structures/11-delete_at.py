#!/usr/bin/python3
"""Module that deletes the item at a specific position in a list."""


def delete_at(my_list=[], idx=0):
    """Remove the item at idx from my_list in place and return it.
    If idx is negative or out of range, the list is left unchanged."""
    if idx < 0 or idx >= len(my_list):
        return my_list
    del my_list[idx]
    return my_list
