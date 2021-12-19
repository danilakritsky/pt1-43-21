"""Tests for the task4."""

import pytest
from task4 import f_of_n
from task4 import sum_of_fs


class TestFofN:
    """Test cases for the `f_of_n` function."""

    @staticmethod
    @pytest.mark.parametrize('test_input', ['a', 1.1, {'a': 3}, (1, 1)])
    def test_invalid_args(test_input):
        """Test for invalid input args."""
        with pytest.raises(TypeError):
            f_of_n(test_input)

    @staticmethod
    @pytest.mark.parametrize('test_input', [0, 1, 10])
    def test_edges(test_input):
        """Test for edge cases."""
        assert f_of_n(test_input) == 0

    @staticmethod
    @pytest.mark.parametrize(
        'test_input, expected',
        [(4, 411728896), (157, 743757)])
    def test_valid(test_input, expected):
        """Test for valid input args."""
        assert f_of_n(test_input) == expected


class TestSumOfFs:
    """Test cases for the `sum_of_fs` function."""

    @staticmethod
    @pytest.mark.parametrize(
        'lower, upper',
        [('a', 1.1), (3, 10.1), ((4, 1), 1)])
    def test_invalid_input(lower, upper):
        """Test for invalid input args."""
        with pytest.raises(TypeError):
            sum_of_fs(lower, upper)

    @staticmethod
    @pytest.mark.parametrize(
        'lower, upper',
        [(1, 0), (10, 5)])
    def test_upper_less_than_lower(lower, upper):
        """Test for invalid arg values: upper < lower."""
        with pytest.raises(ValueError):
            sum_of_fs(lower, upper)

    @staticmethod
    @pytest.mark.parametrize(
        'lower, upper, expected',
        [(0, 1, 0), (2, 10**3, 442530011399)])
    def test_valid_input(lower, upper, expected):
        """Test for valid input args."""
        assert sum_of_fs(lower, upper) == expected
