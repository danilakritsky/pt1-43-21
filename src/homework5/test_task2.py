"""Tests for task2.py."""

import io
import unittest
from unittest.mock import patch

from task2 import main
from task2 import prompt_until_match


class TestPromptUntilMatch(unittest.TestCase):
    """Test case for the prompt_until_match() function."""

    @patch('builtins.input', return_value='match')
    def test_first_prompt(self, mock_input):
        """Test the first input prompt message."""
        prompt_until_match('match', 'prompt', 'fail_msg')
        self.assertIsNone(mock_input.assert_called_with('prompt'))

    @patch('builtins.input', side_effect=['failure', 'match'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_fail_msg(self, mock_stdout, mock_input):
        """Test the print message after a failed match."""
        # pylint: disable=W0613 - disable the unused-argument error for mock_input
        prompt_until_match('match', 'prompt', 'fail_msg')
        self.assertEqual(mock_stdout.getvalue(), 'fail_msg\n')

    @patch('builtins.input', return_value='match')
    def test_return_value(self, mock_input):
        """Test the return value."""
        # pylint: disable=W0613
        result = prompt_until_match('match', 'prompt', 'fail_msg')
        self.assertEqual(result[0], 'match')


class TestMain(unittest.TestCase):
    """Test case for the main() function."""

    @patch('builtins.input', side_effect=[
        '2', 'Belarus Minsk', 'Germany Berlin', '2', 'Minsk', 'Berlin']
    )
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_output(self, mock_stdout, mock_input):
        """Test the output of the main() function."""
        # pylint: disable=W0613
        main()
        self.assertEqual(mock_stdout.getvalue(), 'Belarus\nGermany\n')


if __name__ == '__main__':
    unittest.main()
