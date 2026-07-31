#!/usr/bin/python3
"""Unittests for models.base.Base.
"""
import unittest
import os
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Tests for the Base class."""

    def test_id_public(self):
        """id is set from the given argument."""
        b = Base(12)
        self.assertEqual(b.id, 12)

    def test_id_none_increments(self):
        """id is auto-incremented when not given."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, b1.id + 1)

    def test_id_zero(self):
        """id of 0 is respected (not treated as falsy/None)."""
        b = Base(0)
        self.assertEqual(b.id, 0)

    def test_id_negative(self):
        """A negative id is respected as given."""
        b = Base(-5)
        self.assertEqual(b.id, -5)

    def test_to_json_string_none(self):
        """None returns the string '[]'."""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_empty(self):
        """An empty list returns the string '[]'."""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_list(self):
        """A list of dicts round-trips through JSON correctly."""
        d = [{"a": 1}]
        self.assertEqual(json.loads(Base.to_json_string(d)), d)

    def test_from_json_string_none(self):
        """None returns an empty list."""
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_empty(self):
        """An empty string returns an empty list."""
        self.assertEqual(Base.from_json_string(""), [])

    def test_from_json_string_valid(self):
        """A valid JSON string is parsed back into the original list."""
        d = [{"a": 1}, {"b": 2}]
        s = json.dumps(d)
        self.assertEqual(Base.from_json_string(s), d)

    def test_save_to_file_rectangle(self):
        """save_to_file writes the exact dictionaries of each instance."""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        self.assertTrue(os.path.exists("Rectangle.json"))
        with open("Rectangle.json", "r") as f:
            content = f.read()
        self.assertEqual(
            json.loads(content),
            [r1.to_dictionary(), r2.to_dictionary()])
        os.remove("Rectangle.json")

    def test_save_to_file_none(self):
        """None is treated as an empty list."""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")
        os.remove("Rectangle.json")

    def test_create_rectangle(self):
        """create() rebuilds an equivalent, but distinct, instance."""
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r1), str(r2))
        self.assertIsNot(r1, r2)

    def test_create_square(self):
        """create() works for Square too."""
        s1 = Square(5, 1, 2, 99)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual(str(s1), str(s2))
        self.assertIsNot(s1, s2)

    def test_load_from_file_no_file(self):
        """Missing file returns an empty list."""
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_load_from_file_rectangle(self):
        """load_from_file rebuilds the same Rectangles that were saved."""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        loaded = Rectangle.load_from_file()
        self.assertEqual(len(loaded), 2)
        self.assertEqual(str(loaded[0]), str(r1))
        self.assertEqual(str(loaded[1]), str(r2))
        os.remove("Rectangle.json")

    def test_load_from_file_square(self):
        """load_from_file rebuilds the same Squares that were saved."""
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        Square.save_to_file([s1, s2])
        loaded = Square.load_from_file()
        self.assertEqual(len(loaded), 2)
        self.assertEqual(str(loaded[0]), str(s1))
        self.assertEqual(str(loaded[1]), str(s2))
        os.remove("Square.json")


if __name__ == "__main__":
    unittest.main()
