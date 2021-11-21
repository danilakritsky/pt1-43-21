"""Tests for task7.py."""

import io
import unittest
from unittest.mock import patch
from unittest import TestCase

from task7 import gcd_euclid


class TestGCDEuclid(TestCase):
    """Test cases for the gcd_euclid() function."""

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_message(self, mock_output):
        """Test the function's printed message."""
        gcd_euclid(1, 2)
        self.assertEqual(mock_output.getvalue(), 'GCD of 1 and 2 is 1.\n')

    def test_output(self):
        """Test the outputs of the function."""
        test_data = [
            (0, 0, 0),
            (0, 100, 100),
            (7, 13, 1),
            (5, 10, 5),
            (8, 8, 8)
        ]
        for first_num, second_num, expected_val in test_data:
            with self.subTest():
                self.assertEqual(
                    gcd_euclid(first_num, second_num),
                    expected_val
                )


if __name__ == '__main__':
    unittest.main()
