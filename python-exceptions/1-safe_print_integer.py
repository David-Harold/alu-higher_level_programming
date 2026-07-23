#!/usr/bin/python3
"""Safely prints an integer."""


def safe_print_integer(value):
    """Print value as an integer if possible.

    Returns True if value was an integer and got printed, False otherwise.
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
