#!/usr/bin/python3
"""okay """


class Square:
    """Class documentation"""
    def __init__(self, size=0):
        """Initialize a new Square instance.

        Args:
            size: The size of the square's sides."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculate and return the current square area.

        Returns:
            The area of the square (size squared).
        """
        return self.__size ** 2
