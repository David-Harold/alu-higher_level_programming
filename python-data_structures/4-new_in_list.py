#!/usr/bin/python3
"""Module that replaces an element in a list at a specific position
without modifying the original list."""


def new_in_list(my_list, idx, element):
    """Return a new list with element at idx replaced, without
    modifying the original list. If idx is negative or out of range,
    return a copy of the original list."""
    new_list = my_list[:]
    if idx < 0 or idx >= len(new_list):
        return new_list
    new_list[idx] = element
    return new_list
