"""Tests for task4.py."""

import unittest
from unittest.case import TestCase
from unittest.mock import patch

from ddt import data    # type: ignore
from ddt import ddt     # type: ignore
from ddt import unpack  # type: ignore

from task4 import difference_count


@ddt
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

    @data(
        (list(range(1, 11)), (0, 0)),
        (list(range(6, 16)), (5, 5)),
        (list(range(1, 16)), (0, 5)),
        (list(range(1, 6)), (5, 0))
    )
    @unpack
    def test_output(self, second_list, expected_output) -> None:
        """Test the difference_count() function."""
        first_list = list(range(1, 11))
        self.assertEqual(
            difference_count(first_list, second_list),
            expected_output
        )

    @data(int, (1, 2), [1, 'a', 3])
    def test_wrong_type(self, second_arg):
        """Test for wrong input type."""
        self.assertRaises(TypeError, difference_count, [1, 2], second_arg)


if __name__ == '__main__':
    unittest.main()
