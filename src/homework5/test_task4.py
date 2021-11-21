"""Tests for task4.py."""

import unittest
from unittest.case import TestCase
from unittest.mock import patch

from task4 import difference_count


class TestDifferenceCount(TestCase):
    """Test cases for the difference_count() function."""

    @patch('builtins.print')
    def test_print(self, mock_print):
        """Test the stdout."""
        difference_count([1, 2, 3], [2])
        self.assertIsNone(
            mock_print.assert_called_with(
                'Count of unique items in the first list: 2',
                'Count of unique items in the second list: 0',
                sep='\n'
            )
        )

    def test_output(self) -> None:
        """Test the difference_count() function."""
        first_list = list(range(1, 11))
        test_data = [
            (first_list, (0, 0)),
            (list(range(6, 16)), (5, 5)),
            (list(range(1, 16)), (0, 5)),
            (list(range(1, 6)), (5, 0))
        ]

        for second_list, expected_output in test_data:
            with self.subTest():
                self.assertEqual(
                    difference_count(first_list, second_list),
                    expected_output
                )


if __name__ == '__main__':
    unittest.main()
