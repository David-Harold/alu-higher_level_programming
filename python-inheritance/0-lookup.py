#!/usr/bin/python3
"""Defines a lookup function."""


def lookup(obj):
    """Return the list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        list: The available attributes and methods of obj.
    """
    return dir(obj)
