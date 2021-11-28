"""Tests for task7.py."""

import io
import unittest
from unittest.mock import patch
from unittest import TestCase

from ddt import data    # type: ignore
from ddt import ddt     # type: ignore
from ddt import unpack  # type: ignore

from task7 import gcd_euclid


@ddt
class TestGCDEuclid(TestCase):
    """Test cases for the gcd_euclid() function."""

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_message(self, mock_output):
        """Test the function's printed message."""
        gcd_euclid(1, 2)
        self.assertEqual(mock_output.getvalue(), 'GCD of 1 and 2 is 1.\n')

    @data((0, 0, 0), (0, 100, 100), (7, 13, 1), (5, 10, 5), (8, 8, 8))
    @unpack
    def test_output(self, first_num, second_num, expected):
        """Test the outputs of the function."""
        self.assertEqual(gcd_euclid(first_num, second_num), expected)

    @data(int, [1, 2], (1, 2), 23.50)
    def test_wrong_type(self, second_num):
        """Test for the error raised by wrong argument type."""
        self.assertRaises(TypeError, gcd_euclid, 10, second_num)


if __name__ == '__main__':
    unittest.main()
