"""Tests for task3.py."""

import unittest
from unittest.case import TestCase
from unittest.mock import patch

from task3 import intersection_count


class TestIntersectionCount(TestCase):
    """Test cases for the intersection_count() function."""

    @patch('builtins.print')
    def test_print(self, mock_print):
        """Test the stdout."""
        intersection_count([1, 2, 3], [2])
        self.assertIsNone(
            mock_print.assert_called_with('Count of unique items: 1')
        )

    def test_output(self) -> None:
        """Test the intersection_count() function."""
        first_list = list(range(1, 11))
        empty_list: list = []
        test_data = [
            (empty_list, 0),
            (first_list[:5], 5),
            (first_list[-3:], 3),
            (first_list[::3], 4),
            (first_list * 3, 10)
        ]

        for second_list, expected_output in test_data:
            with self.subTest():
                self.assertEqual(
                    intersection_count(first_list, second_list),
                    expected_output
                )


if __name__ == '__main__':
    unittest.main()
