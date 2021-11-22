"""Tests for task3.py."""

import unittest
from unittest import TestCase

from ddt import ddt, data, unpack  # type: ignore

from task3 import get_ranges
from task3 import validate_input
from task3 import ArgumentError


@ddt
class TestValidateInput(TestCase):
    """Test case for the validate_input() function."""

    @data(1, int, (1, 2), [], [1, '2'], [1, 0, -1])
    def test_bad_input(self, user_input):
        """Test for bad input."""
        self.assertFalse(validate_input(user_input))

    @data([1], [2, 3], [1, 2, 5, 8])
    def test_proper_input(self, user_input):
        """Test for proper input."""
        self.assertTrue(validate_input(user_input))


@ddt
class TestGetRanges(TestCase):
    """Test cases for the get_ranges() function."""

    @data(1, int, (1, 2), [], [1, '2'], [1, 0, -1])
    def test_bad_input(self, user_input):
        """Test for bad input."""
        self.assertRaises(ArgumentError, get_ranges, user_input)

    @data(
        ([1, 2, 3], '1-3'),
        ([1, 3, 7], '1,3,7'),
        ([1], '1'),
        ([4, 5, 6, 8, 11, 14, 15, 16, 17], '4-6,8,11,14-17'))
    @unpack
    def test_output(self, user_input, output):
        """Test for proper output."""
        self.assertEqual(get_ranges(user_input), output)


if __name__ == '__main__':
    unittest.main()
