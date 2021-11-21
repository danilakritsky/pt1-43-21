"""Tests for task1.py."""

import unittest

from task1 import main


class TestMain(unittest.TestCase):
    """Test case for the main() function."""

    def test_type(self):
        """Test the type of the ojbect returned by main()."""
        result = main()
        self.assertIsInstance(result, dict)

    def test_keys(self):
        """Test the keys of the dictionary returned by main()."""
        result = main()
        self.assertEqual(list(result.keys()), list(range(1, 21)))

    def test_values(self):
        """Test values of the of the dictionary returned by main()."""
        result = main()
        self.assertEqual(
            list(result.values()),
            list(map(lambda x: pow(x, 3), list(range(1, 21))))
        )


if __name__ == '__main__':
    unittest.main()
