import inspect
import pathlib
import re
import functools
from collections import defaultdict
import json

CALL_HISTORY_CACHE = pathlib.Path('task2_cache')

def init_db():
    if CALL_HISTORY_CACHE.exists():
        return
    with CALL_HISTORY_CACHE.open('w') as f:
        json.dump({}, f)

init_db()

def remove_decorator_sugar(source: str) -> str:
    return re.sub(r'@\w+\n', '', source)


def load_history() -> dict:
    with CALL_HISTORY_CACHE.open('r') as f:
        return json.load(f)


def update_db(func):
    call_history_dict = load_history()
    call_history_dict[inspect.getsource(func)] = func.call_history
    with open(CALL_HISTORY_CACHE, 'w') as f:
        json.dump(call_history_dict, f)


def get_call_history(func):
    with open(CALL_HISTORY_CACHE, 'r') as f:
        call_history_dict = load_history()
        history = call_history_dict.get(inspect.getsource(func), [])
        func.call_history = history


# TODO call history (time?)
def cache_results(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        get_call_history(func)
        result = func(*args, **kwargs)
        func.call_history.append(result)
        update_db(func)
        return result
    return wrapper


@cache_results
def test():
    return 1


test()


