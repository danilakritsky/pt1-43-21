"""Tests for task5.py."""

import io
import unittest
from unittest.case import TestCase
from unittest.mock import patch

from task5 import main


class TestMain(TestCase):
    """Test case for the main() function."""

    @patch(
        'builtins.input',
        side_effect=[
            '3',
            '2', 'Russian', 'English',
            '2', 'German', 'Russian',
            '1', 'Russian'
        ]
    )
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_output(self, mock_stdout, mock_input):
        """Test the output of the main() function."""
        # pylint: disable=W0613
        main()
        self.assertEqual(
            mock_stdout.getvalue(),
            "Languages all the students know:\nRussian\n"
            "Languages only some students know:\nEnglish\nGerman\n"
        )


if __name__ == '__main__':
    unittest.main()
