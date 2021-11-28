"""Tests for task6.py."""

import io
import unittest
from unittest.mock import patch
from unittest import TestCase

from task6 import main


class TestMain(TestCase):
    """Tests for the main() function."""

    @patch('builtins.input', side_effect=[''])
    def test_no_input(self, _):
        """Test the output of main() when no text is input."""
        self.assertRaises(SystemExit, main)

    @patch('builtins.input', side_effect=['cat dog cat', 'dog cat bird', ''])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_output(self, mock_stdout, _):
        """Test the output of the main() function."""
        main()
        self.assertEqual(mock_stdout.getvalue(), "Unique words count: 3\n")


if __name__ == '__main__':
    unittest.main()
