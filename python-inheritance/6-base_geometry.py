#!/usr/bin/python3
"""Defines a BaseGeometry class."""


class BaseGeometry:
    """Represent a base for geometric objects."""

    def area(self):
        """Raise an Exception; area() must be implemented by subclasses."""
        raise Exception("area() is not implemented")
