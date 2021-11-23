"""Бинарные операции.

Написать программу которая находит ближайшую степень двойки к
введенному числу. 10(8), 20(16), 1(1), 13(16)
"""

import functools
from typing import Callable


def printout(func: Callable) -> Callable:
    """A decorator that prints a message before returning result."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, tuple):
            print(f"The closest power of two to {args[0]} are {result[0]} and {result[1]}.")
        else:
            print(f"The closest power of two to {args[0]} is {result}.")
        return result
    return wrapper


@printout
def closest_pow_of_two(num: int) -> int | tuple[int, int]:
    """Find the closest power of two for a given number.

    Returns a tuple if the number is equidistant from both next and previous power of two.
    """
    if not isinstance(num, int):
        raise TypeError('Expected an integer.')
    if num < 0:
        raise ValueError('Only positive integers are allowed.')

    if num == 0:
        return 1
    if num & (num - 1) == 0:  # 8 & 7 -> 1000 & 0111 = 0
        return num

    prev_pow = num
    while (mask := prev_pow & (prev_pow - 1)):
        prev_pow = mask
    next_pow = prev_pow << 1

    if num == (next_pow + prev_pow) >> 1:  # if num is equidistant from both powers
        return prev_pow, next_pow

    return prev_pow if (num - prev_pow) < (next_pow - num) else next_pow
