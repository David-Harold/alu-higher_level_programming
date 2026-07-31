#!/usr/bin/python3
"""Defines an is_kind_of_class function."""


def is_kind_of_class(obj, a_class):
    """Return True if obj is an instance of a_class or of a subclass.

    Args:
        obj: The object to check.
        a_class (type): The class to check against.

    Returns:
        bool: True if obj is an instance of a_class or a subclass.
    """
    return isinstance(obj, a_class)
