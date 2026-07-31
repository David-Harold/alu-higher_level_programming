#!/usr/bin/python3
"""Unittests for models.square.Square.
"""
import unittest
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """Tests for the Square class."""

    def test_is_rectangle_subclass(self):
        """Square inherits from Rectangle."""
        s = Square(5)
        self.assertIsInstance(s, Rectangle)

    def test_width_equals_height(self):
        """width and height are always equal for a Square."""
        s = Square(5)
        self.assertEqual(s.width, s.height)

    def test_default_x_y(self):
        """x and y default to 0."""
        s = Square(5)
        self.assertEqual((s.x, s.y), (0, 0))

    def test_all_attributes(self):
        """All constructor arguments land on the right attribute."""
        s = Square(3, 1, 3, 7)
        self.assertEqual(
            (s.id, s.width, s.height, s.x, s.y), (7, 3, 3, 1, 3))

    def test_area(self):
        """area() returns size * size."""
        self.assertEqual(Square(5).area(), 25)

    def test_str(self):
        """__str__ matches the documented [Square] format exactly."""
        s = Square(5)
        self.assertEqual(str(s), "[Square] ({}) 0/0 - 5".format(s.id))

    def test_size_getter(self):
        """size getter mirrors width."""
        s = Square(5)
        self.assertEqual(s.size, 5)

    def test_size_setter(self):
        """size setter updates both width and height."""
        s = Square(5)
        s.size = 10
        self.assertEqual((s.width, s.height), (10, 10))

    def test_size_setter_type_error(self):
        """size setter reuses width's TypeError message."""
        s = Square(5)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.size = "9"

    def test_size_setter_value_error(self):
        """size setter reuses width's ValueError message."""
        s = Square(5)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.size = -1

    def test_update_args(self):
        """update() with positional args maps to id, size, x, y."""
        s = Square(5)
        s.update(1, 2, 3, 4)
        self.assertEqual((s.id, s.size, s.x, s.y), (1, 2, 3, 4))

    def test_update_kwargs(self):
        """update() accepts keyword arguments in any order."""
        s = Square(5)
        s.update(size=7, id=89, y=1)
        self.assertEqual((s.id, s.size, s.y), (89, 7, 1))

    def test_to_dictionary(self):
        """to_dictionary returns exactly id, size, x, y."""
        s = Square(10, 2, 1, 1)
        self.assertEqual(
            s.to_dictionary(), {"id": 1, "size": 10, "x": 2, "y": 1})

    def test_to_dictionary_round_trip(self):
        """A dictionary can rebuild an equivalent Square via update."""
        s1 = Square(10, 2, 1)
        s2 = Square(1, 1)
        s2.update(**s1.to_dictionary())
        self.assertEqual(str(s1), str(s2))

    def test_inherits_rectangle_validation(self):
        """Square reuses Rectangle's width/height validation as-is."""
        with self.assertRaises(TypeError):
            Square("5")
        with self.assertRaises(ValueError):
            Square(-5)


if __name__ == "__main__":
    unittest.main()
