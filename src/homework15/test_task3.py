"""Tests for task3.py."""

import pytest
from task3 import get_count_by_case


@pytest.mark.parametrize('user_input', [False, True, 1, 1.0])
def test_type_error_for_non_iterables(user_input):
    """Test for non-iterable input."""
    with pytest.raises(TypeError):
        get_count_by_case(user_input)


@pytest.mark.parametrize(
    'user_input',
    [func([False, True, 1, 1.0]) for func in (tuple, list, set, dict.fromkeys)])  # type: ignore
def test_type_error_for_iterables(user_input):
    """Test for iterable input with wrong types."""
    with pytest.raises(TypeError):
        get_count_by_case(user_input)


def test_empty_str():
    """Test for empty string input."""
    assert get_count_by_case('') == (0, 0)


@pytest.mark.parametrize('user_input', ['$!%@#', 'привет', '12'])
def test_non_english(user_input):
    """Test for non-english characters."""
    assert get_count_by_case(user_input) == (0, 0)


@pytest.mark.parametrize('user_input', ['christmas', 'airplane', 'fox'])
def test_only_lower(user_input):
    """Test for lowercase-only input."""
    assert get_count_by_case(user_input) == (len(user_input), 0)


@pytest.mark.parametrize('user_input', ['DOG', 'CAT', 'PHONE'])
def test_only_upper(user_input):
    """Test for uppercase-only input."""
    assert get_count_by_case(user_input) == (0, len(user_input))


@pytest.mark.parametrize(
    'user_input, expected',
    [('Aqua!', (3, 1)), ('FaceBook', (6, 2)), ('The End', (4, 2))])
def test_mixed(user_input, expected):
    """Test for mixed input."""
    assert get_count_by_case(user_input) == expected
