"""Tests for task4.py."""

import unittest
from unittest import TestCase

from ddt import ddt, data, unpack  # type: ignore

from task4 import sum_of_bin_repr


@ddt
class TestSumOfBinRepr(TestCase):
    """Test case for the sum_of_bin_repr() function."""

    @data((None, None), ('a', []), (1, tuple))
    @unpack
    def test_wrong_type(self, start, end):
        """Test for wrong argument types."""
        self.assertRaises(TypeError, sum_of_bin_repr, start, end)

    @data((-1, 0), (1, 0), (100, -100))
    @unpack
    def test_wrong_values(self, start, end):
        """Test for invalid argument values."""
        self.assertRaises(ValueError, sum_of_bin_repr, start, end)

    @data((1, 4, '1111010'), (2, 3, '10101'), (5, 7, '101000010'))
    @unpack
    def test_output(self, start, end, expected):
        """Test for the output of the function."""
        self.assertEqual(sum_of_bin_repr(start, end), expected)


if __name__ == '__main__':
    unittest.main()
