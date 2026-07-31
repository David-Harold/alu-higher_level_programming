#!/usr/bin/python3
"""Defines an is_same_class function."""


def is_same_class(obj, a_class):
    """Return True if obj is exactly an instance of a_class.

    Args:
        obj: The object to check.
        a_class (type): The class to check against.

    Returns:
        bool: True if type(obj) is a_class, otherwise False.
    """
    return type(obj) is a_class
