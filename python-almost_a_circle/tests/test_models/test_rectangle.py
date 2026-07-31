#!/usr/bin/python3
"""Unittests for models.rectangle.Rectangle.
"""
import unittest
from io import StringIO
from unittest.mock import patch
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Tests for the Rectangle class."""

    def test_is_base_subclass(self):
        """Rectangle inherits from Base."""
        r = Rectangle(1, 1)
        self.assertIsInstance(r, Base)

    def test_default_x_y(self):
        """x and y default to 0."""
        r = Rectangle(2, 3)
        self.assertEqual((r.x, r.y), (0, 0))

    def test_all_attributes(self):
        """All constructor arguments land on the right attribute."""
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(
            (r.id, r.width, r.height, r.x, r.y), (5, 1, 2, 3, 4))

    def test_width_type_error(self):
        """A non-integer width raises TypeError with the exact message."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("2", 2)

    def test_height_type_error(self):
        """A non-integer height raises TypeError with the exact message."""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, "2")

    def test_x_type_error(self):
        """A non-integer x raises TypeError with the exact message."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 2, {})

    def test_y_type_error(self):
        """A non-integer y raises TypeError with the exact message."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 2, 0, [])

    def test_width_value_error(self):
        """width <= 0 raises ValueError with the exact message."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)

    def test_height_value_error(self):
        """height <= 0 raises ValueError with the exact message."""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(2, -1)

    def test_x_value_error(self):
        """x < 0 raises ValueError with the exact message."""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(2, 2, -1)

    def test_y_value_error(self):
        """y < 0 raises ValueError with the exact message."""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(2, 2, 0, -1)

    def test_width_setter(self):
        """The width setter updates the value."""
        r = Rectangle(1, 1)
        r.width = 10
        self.assertEqual(r.width, 10)

    def test_width_setter_bad(self):
        """The width setter still validates on reassignment."""
        r = Rectangle(1, 1)
        with self.assertRaises(ValueError):
            r.width = -10

    def test_area(self):
        """area() returns width * height."""
        self.assertEqual(Rectangle(3, 2).area(), 6)
        self.assertEqual(Rectangle(8, 7, 0, 0, 12).area(), 56)

    def test_display_no_offset(self):
        """display() with x=0, y=0 prints a plain block."""
        r = Rectangle(2, 2)
        expected = "##\n##\n"
        with patch("sys.stdout", new=StringIO()) as out:
            r.display()
            self.assertEqual(out.getvalue(), expected)

    def test_display_with_x_offset(self):
        """display() indents each row by x spaces."""
        r = Rectangle(3, 2, 1, 0)
        expected = " ###\n ###\n"
        with patch("sys.stdout", new=StringIO()) as out:
            r.display()
            self.assertEqual(out.getvalue(), expected)

    def test_display_with_y_offset(self):
        """display() prints y blank lines before the block."""
        r = Rectangle(2, 3, 2, 2)
        expected = "\n\n  ##\n  ##\n  ##\n"
        with patch("sys.stdout", new=StringIO()) as out:
            r.display()
            self.assertEqual(out.getvalue(), expected)

    def test_str(self):
        """__str__ matches the documented format exactly."""
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_update_args_id_only(self):
        """update() with one positional arg only updates id."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89)
        self.assertEqual(r.id, 89)

    def test_update_args_all(self):
        """update() with 5 positional args updates every attribute."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(
            (r.id, r.width, r.height, r.x, r.y), (89, 2, 3, 4, 5))

    def test_update_kwargs(self):
        """update() accepts keyword arguments in any order."""
        r = Rectangle(10, 10, 10, 10)
        r.update(y=1, width=2, x=3, id=89)
        self.assertEqual(
            (r.id, r.width, r.height, r.x, r.y), (89, 2, 10, 3, 1))

    def test_update_args_priority_over_kwargs(self):
        """kwargs are ignored entirely if args is non-empty."""
        r = Rectangle(10, 10)
        r.update(1, 2, 3, 4, 5, height=100)
        self.assertEqual(r.height, 3)

    def test_to_dictionary(self):
        """to_dictionary returns exactly the 5 expected keys."""
        r = Rectangle(10, 2, 1, 9, 2)
        d = r.to_dictionary()
        self.assertEqual(
            d, {"id": 2, "width": 10, "height": 2, "x": 1, "y": 9})

    def test_to_dictionary_round_trip(self):
        """A dictionary can rebuild an equivalent Rectangle via update."""
        r1 = Rectangle(10, 2, 1, 9)
        r2 = Rectangle(1, 1)
        r2.update(**r1.to_dictionary())
        self.assertEqual(str(r1), str(r2))


if __name__ == "__main__":
    unittest.main()
