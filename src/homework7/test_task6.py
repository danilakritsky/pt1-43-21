"""Tests for task6.py."""

import unittest
from unittest import TestCase

from ddt import data    # type: ignore
from ddt import ddt     # type: ignore
from ddt import unpack  # type: ignore

from task6 import closest_pow_of_two

# TODO(Danila): printout test


@ddt
class TestSumOfBinRepr(TestCase):
    """Test case for the closest_pow_of_two() function."""

    @data(None, int, [1, 3], '1')
    def test_wrong_type(self, arg):
        """Test for wrong argument types."""
        self.assertRaises(TypeError, closest_pow_of_two, arg)

    @data(-1, -100)
    def test_negative_int(self, arg):
        """Test for negative integer input."""
        self.assertRaises(ValueError, closest_pow_of_two, arg)

    @data((0, 1), (4, 4), (6, (4, 8)))
    @unpack
    def test_edges(self, arg, expected):
        """Test for the edge cases."""
        self.assertEqual(closest_pow_of_two(arg), expected)

    @data((13, 16), (10, 8), (21, 16))
    @unpack
    def test_output(self, arg, expected):
        """Test for the output."""
        self.assertEqual(closest_pow_of_two(arg), expected)


if __name__ == '__main__':
    unittest.main()
