#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Tests for the max_integer function"""

    def test_ordered_list(self):
        """Ascending list"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Unordered list"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_descending_list(self):
        """Descending list"""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_single_element(self):
        """Single element list"""
        self.assertEqual(max_integer([5]), 5)

    def test_empty_list(self):
        """Empty list returns None"""
        self.assertIsNone(max_integer([]))

    def test_no_argument(self):
        """No argument uses the default (empty list), returns None"""
        self.assertIsNone(max_integer())

    def test_negative_numbers(self):
        """All negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3]), -1)

    def test_mixed_positive_negative(self):
        """Mix of positive and negative numbers"""
        self.assertEqual(max_integer([-5, 0, 5, -10, 3]), 5)

    def test_all_same_values(self):
        """All elements identical"""
        self.assertEqual(max_integer([2, 2, 2, 2]), 2)

    def test_floats(self):
        """List of floats"""
        self.assertEqual(max_integer([1.5, 2.5, 0.5]), 2.5)


if __name__ == "__main__":
    unittest.main()
