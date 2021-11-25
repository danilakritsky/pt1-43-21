"""Декоратор для хранения результатов вызовов.

Создайте декоратор, который хранит результаты вызовов функции (за
все время вызовов, не только текущий запуск программы)
"""

import functools
import inspect
import json
import pathlib
import re
from typing import Any
from typing import Callable

ENCODING = 'utf-8'
CALL_HISTORY_CACHE = pathlib.Path('task2_cache')

# pylint: disable = W0511
# TODO: refactor - move functions to a class, add a method to clear history
# TODO: make decorator return a new function-like class with an attribute to pass mypy checks


def init_db() -> None:
    """Initialize a database to keep function call results."""
    if CALL_HISTORY_CACHE.exists():
        return
    with CALL_HISTORY_CACHE.open('w', encoding=ENCODING) as file:
        json.dump({}, file)


init_db()


def load_history() -> dict[str, list[Any]]:
    """Read the function call database and return its contents."""
    with CALL_HISTORY_CACHE.open('r', encoding=ENCODING) as dbase:
        return json.load(dbase)


def get_func_id(func: Callable) -> str:
    """Return the function's id as a str.

    Id is a string representation of a tuple of the function's name, module and source code.
    """
    src = inspect.getsource(func)
    src_no_decor = re.sub(r'@\w*cache_results\n', '', src)  # remove the cache decorator from code
    return f'{func.__name__, func.__module__, src_no_decor}'


def update_db(func: Callable) -> None:
    """Update the call results history of a function."""
    call_history_dict = load_history()
    call_history_dict[get_func_id(func)] = func.call_history
    with open(CALL_HISTORY_CACHE, 'w', encoding=ENCODING) as file:
        json.dump(call_history_dict, file)


def get_call_history(func: Callable) -> list[Any]:
    """Get the call results history of a function."""
    with open(CALL_HISTORY_CACHE, 'r', encoding=ENCODING):
        call_history_dict = load_history()
        history = call_history_dict.get(get_func_id(func), [])
        return history


def cache_results(func: Callable):
    """Store results of each call of a function in a file database."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        history = get_call_history(func)
        result = func(*args, **kwargs)
        history.append(result)
        func.call_history = wrapper.call_history = history
        update_db(func)
        return result
    wrapper.call_history = get_call_history(func)
    return wrapper


if __name__ == '__main__':
    @cache_results
    def test_cache() -> str:
        """Return called."""
        return 'Called.'

    assert test_cache.call_history == []
    for call_num in range(1, 11):
        test_cache()
    assert test_cache.call_history == ['Called.'] * call_num
    print('Tests passed.')
