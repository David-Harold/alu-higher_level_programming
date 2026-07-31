#!/usr/bin/python3
"""Defines an inherits_from function."""


def inherits_from(obj, a_class):
    """Return True if obj's class is a subclass of a_class.

    Args:
        obj: The object to check.
        a_class (type): The class to check against.

    Returns:
        bool: True if obj is an instance of a class that inherited
        (directly or indirectly) from a_class, otherwise False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
