"""Tests for task5.py."""

import io
import unittest
from unittest.case import TestCase
from unittest.mock import patch

from task5 import get_language_data
from task5 import print_language_data


class TestGetLanguageData(TestCase):
    """Test case for the get_language_data() function."""

    @patch(
        'builtins.input',
        side_effect=[
            '3',
            '2', 'Russian', 'English',
            '2', 'German', 'Russian',
            '1', 'Russian'
        ])
    def test_output(self, _):
        """Test the output of the function."""
        result = get_language_data()
        self.assertEqual(
            (sorted(result[0]), result[1]),
            (sorted(['English', 'German', 'Russian', 'Russian', 'Russian']), 3)
        )


class TestPrintLanguageData(TestCase):
    """Test case for the print_language_data() function."""

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_output(self, mock_stdout):
        """Test the output of the print_language_data() function."""
        print_language_data(['English', 'German', 'Russian', 'Russian', 'Russian'], 3)
        self.assertEqual(
            mock_stdout.getvalue(),
            "Languages all the students know:\nRussian\n"
            "Languages only some students know:\nEnglish\nGerman\n"
        )


if __name__ == '__main__':
    unittest.main()
