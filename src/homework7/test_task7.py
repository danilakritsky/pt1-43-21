"""Tests for task7.py."""

import unittest
from unittest import TestCase

from ddt import ddt     # type: ignore
from ddt import data    # type: ignore
from ddt import unpack  # type: ignore

from task7 import greatest_divisor


@ddt
class TestGreatestDivisor(TestCase):
    """Test case for the greatest_divisor() function."""

    @data(None, int, [1, 1], '1')
    def test_wrong_type(self, arg):
        """Test for wrong argument types."""
        self.assertRaises(TypeError, greatest_divisor, arg)

    @data(-1, -100)
    def test_negative_int(self, arg):
        """Test for negative integer input."""
        self.assertRaises(ValueError, greatest_divisor, arg)

    @data((1, 1), (4, 4), (32, 32))
    @unpack
    def test_edges(self, arg, expected):
        """Test for the edge cases."""
        self.assertEqual(greatest_divisor(arg), expected)

    @data((6, 2), (20, 4), (48, 16))
    @unpack
    def test_output(self, arg, expected):
        """Test for the output."""
        self.assertEqual(greatest_divisor(arg), expected)


if __name__ == '__main__':
    unittest.main()
