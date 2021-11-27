"""Tests for task3.py."""

import unittest
from unittest.case import TestCase
from unittest.mock import patch

from ddt import data    # type: ignore
from ddt import ddt     # type: ignore
from ddt import unpack  # type: ignore

from task3 import intersection_count


@ddt
class TestIntersectionCount(TestCase):
    """Test cases for the intersection_count() function."""

    @patch('builtins.print')
    def test_print(self, mock_print):
        """Test the stdout."""
        intersection_count([1, 2, 3], [2])
        self.assertIsNone(
            mock_print.assert_called_with('Count of unique items: 1')
        )

    @data(
        ([], 0),
        ([1, 2, 3, 4, 5], 5),
        ([8, 9, 10], 3),
        ([1, 4, 7, 10], 4),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10] * 3, 10)
    )
    @unpack
    def test_output(self, second_list, expected_output):
        """Test the intersection_count() function."""
        first_list = list(range(1, 11))
        self.assertEqual(
            intersection_count(first_list, second_list),
            expected_output
        )

    @data(int, (1, 2), [1, 'a', 3])
    def test_wrong_type(self, second_arg):
        """Test for wrong input type."""
        self.assertRaises(TypeError, intersection_count, [1, 2], second_arg)


if __name__ == '__main__':
    unittest.main()
