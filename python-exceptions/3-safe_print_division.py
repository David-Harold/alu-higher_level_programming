#!/usr/bin/python3
"""Divides two integers safely."""


def safe_print_division(a, b):
    """Divide a by b, printing debug info in the finally clause.

    Returns the division result, or None if division by zero occurred.
    """
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
