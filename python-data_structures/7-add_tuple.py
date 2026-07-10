#!/usr/bin/python3
"""Module that adds 2 tuples."""


def add_tuple(tuple_a=(), tuple_b=()):
    """Return a tuple of 2 integers, the element-wise sum of the first
    2 values of each argument. Missing values are treated as 0."""
    a0 = tuple_a[0] if len(tuple_a) > 0 else 0
    a1 = tuple_a[1] if len(tuple_a) > 1 else 0
    b0 = tuple_b[0] if len(tuple_b) > 0 else 0
    b1 = tuple_b[1] if len(tuple_b) > 1 else 0
    return (a0 + b0, a1 + b1)
