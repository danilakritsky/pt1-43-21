"""Tests for task2.py."""

import pytest
from task2 import limit_calls
from task2 import TooManyErrors


def _test_func(num):
    return num + 1


@pytest.fixture(name='limit')
def fixture_limit():
    """Return the function call limit to be used by the limit_calls decorator."""
    return 3


@pytest.fixture(name='decorated_by_call_limit')
def fixture_decorated_by_call_limit(limit):
    """Return the _test_func decorator with the limit_calls decorator."""
    return limit_calls(limit)(_test_func)


def test_pass_on_first_call(decorated_by_call_limit):
    """Test for 2 consecutive valid args calls."""
    func = decorated_by_call_limit
    assert func(1) == 2  # success
    # 2nd call after success returns the first successful value
    assert func(2) == 2


def test_pass_on_second_call(decorated_by_call_limit):
    """Test for first calling func with invalid args followed by valid args."""
    func = decorated_by_call_limit
    assert isinstance(func('1'), Exception)  # raised exception of first call
    assert func(1) == 2  # next call suceeds


def test_fail_on_third_call(decorated_by_call_limit, capsys):
    """Test for 3 consecutive calls with invalid args."""
    func = decorated_by_call_limit
    assert isinstance(func('1'), Exception)
    assert isinstance(func('2'), Exception)
    result = func('3')
    out, _ = capsys.readouterr()
    # 3rd unsuccesful call returns fail message
    error_msg = 'Function failed.\n'
    assert out[-len(error_msg):] == error_msg
    assert isinstance(result, Exception)


def test_raises_too_many_errors(decorated_by_call_limit):
    """Test for TooManyError raised after 4 consecutive calls with invalid args."""
    func = decorated_by_call_limit
    with pytest.raises(TooManyErrors):
        for _ in range(4):
            func('1')
