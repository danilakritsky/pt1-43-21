"""Tests for task2.py."""

import io
import unittest
from unittest.mock import patch

from task2 import prompt_until_match
from task2 import query_data
from task2 import store_data


class TestPromptUntilMatch(unittest.TestCase):
    """Test case for the prompt_until_match() function."""

    @patch('builtins.input', return_value='match')
    def test_first_prompt(self, mock_input):
        """Test the first input prompt message."""
        prompt_until_match('match', 'prompt', 'fail_msg')
        self.assertIsNone(mock_input.assert_called_with('prompt'))

    @patch('builtins.input', side_effect=['failure', 'match'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_fail_msg(self, mock_stdout, _):
        """Test the print message after a failed match."""
        prompt_until_match('match', 'prompt', 'fail_msg')
        self.assertEqual(mock_stdout.getvalue(), 'fail_msg\n')

    @patch('builtins.input', return_value='match')
    def test_return_value(self, _):
        """Test the return value."""
        result = prompt_until_match('match', 'prompt', 'fail_msg')
        self.assertEqual(result[0], 'match')


class TestStoreData(unittest.TestCase):
    """Test case for the store_data() function."""

    @patch('builtins.input', side_effect=['2', 'Belarus Minsk', 'Germany Berlin'])
    def test_output(self, _):
        """Test the output of the store_data() function."""
        result = store_data()
        self.assertEqual(result, {'Minsk': 'Belarus', 'Berlin': 'Germany'})


class TestQueryData(unittest.TestCase):
    """Test case for the main() function."""

    @patch('builtins.input', side_effect=['2', 'Minsk', 'Berlin'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_output(self, mock_stdout, _):
        """Test the output of the query_data() function."""
        query_data({'Minsk': 'Belarus', 'Berlin': 'Germany'})
        self.assertEqual(mock_stdout.getvalue(), 'Belarus\nGermany\n')

    @patch('builtins.input', side_effect=['2', '"New York"', 'Rome'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_nonexistent_city(self, mock_stdout, _):
        """Test the output of the query_data() function when a city is not found."""
        query_data({'Minsk': 'Belarus', 'Berlin': 'Germany'})
        self.assertEqual(mock_stdout.getvalue(), 'City not found.\n' * 2)


if __name__ == '__main__':
    unittest.main()
