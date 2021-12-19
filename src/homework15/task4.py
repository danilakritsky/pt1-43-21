"""Project Euler #455 - Powers With Trailing Digits.

https://projecteuler.net/problem=455
Let f(n) be the largest positive integer x less than 10**9 such that
the last 9 digits of n**x form the number x (including leading zeros),
or zero if no such integer exists.

For example:

f(4) = 411728896 (4411728896 = ...490411728896)
f(10) = 0
f(157) = 743757 (157743757 = ...567000743757)
∑f(n), 2 ≤ n ≤ 10**3 = 442530011399
Find ∑f(n), 2 ≤ n ≤ 10**6.
"""

# pylint: disable=bad-option-value,W503
import functools
import inspect
import time
from typing import Callable


ESCAPE_CHAR: str = '\x1B'
NORMAL: str = ESCAPE_CHAR + '[0m'
BOLD: str = ESCAPE_CHAR + '[1m'
ITALICS: str = ESCAPE_CHAR + '[3m'
SAVE_CURSOR_POSITION: str = ESCAPE_CHAR + '[s'
LOAD_CURSOR_POSITION: str = ESCAPE_CHAR + '[u'
FONT_COLOR: str = ESCAPE_CHAR + '[38;5;{code}m'
BLACK_FONT: str = FONT_COLOR.format(code=0)
RED_FONT: str = FONT_COLOR.format(code=167)
BLUE_FONT: str = FONT_COLOR.format(code=39)
BACKGROUND_COLOR: str = ESCAPE_CHAR + '[48;5;{code}m'
WHITE_BACKGROUND: str = BACKGROUND_COLOR.format(code=231)


def log_time(func: Callable) -> Callable:
    """Log how much time the function call took."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        arg_dict: dict = inspect.signature(func).bind(*args, **kwargs).arguments
        arg_str = '(' + ', '.join(f'{param}={val}' for param, val in arg_dict.items()) + ')'
        print(
            f'{ITALICS}Calling{NORMAL}'
            ' '
            f'{WHITE_BACKGROUND}{RED_FONT}{func.__name__}{arg_str}{NORMAL}...')
        start = time.time()
        result = func(*args, **kwargs)
        print(
            f'\n{ITALICS}Finished.{NORMAL}',
            f'Time elapsed: {BLUE_FONT}{time.time() - start:0.2f} sec{NORMAL}',
            f'Result: {WHITE_BACKGROUND}{BLACK_FONT}{BOLD}{result:,}{NORMAL}',
            sep='\n')
        return result
    return wrapper


def f_of_n(num: int) -> int:
    """Find f(n) as defined in the module docstring.

    Based on the C++ solution described @ https://euler.stephan-brumme.com/455/.
    """
    if not isinstance(num, int):
        raise TypeError('Expected int.')

    if num % 10 == 0 or num == 1:
        return 0
    power = num
    while (trailing_digits := pow(num, power, 10 ** 9)) != power:
        power = trailing_digits
    return power


@log_time
def sum_of_fs(lower: int = 2, upper: int = 10**6) -> int:
    """Find the sum of f(n) for `lower` ≤ n ≤ `upper`."""
    if not all((isinstance(arg, int) for arg in (lower, upper))):
        raise TypeError('Expected int.')

    if upper < lower:
        raise ValueError('`upper` must be `greater` than lower.')

    total = 0
    for num in range(lower, upper + 1):
        total += f_of_n(num)
        print(_num_to_progress_bar(num, lower, upper), end=LOAD_CURSOR_POSITION, flush=False)
    return total


def _num_to_progress_bar(cur_num: int, min_num: int, max_num: int, bar_width: int = 20) -> str:
    """Create a progress bar given a min, max and current number."""
    progress_bar = (
        SAVE_CURSOR_POSITION
        + '['
        + ('#' * (cur_iter := int(
            (cur_pct := (cur_num - min_num) / (max_num - min_num)) * bar_width)))
        + (bar_width - cur_iter) * ' '
        + ']'
        + ' '
        + f'{cur_pct * 100:0.1f}%'
    )
    return progress_bar


if __name__ == '__main__':
    sum_of_fs(2, 10**4)
