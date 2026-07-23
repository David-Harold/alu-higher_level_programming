#!/usr/bin/python3
"""okay """


class Square:
    """Class documentation"""
    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square instance.

        Args:
            size: The size of the square's sides."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with type and value validation.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """retrieve the value of property as it is encapusulated"""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the quare with
        type and value validation"""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not isinstance(value[0], int) or
                not isinstance(value[1], int) or
                value[0] < 0 or
                value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate and return the current square area.

        Returns:
            The area of the square (size squared).
        """
        return self.__size ** 2

    def my_print(self):
        """Public instatnce method that prints in stout the square
        with the character #"""
        if self.__size == 0:
            print()
            return
        for _ in range(self.__position[1]):
            print()
        for _ in range(1, self.__size + 1):
            print(" " * self.__position[0] + "#" * self.__size)
