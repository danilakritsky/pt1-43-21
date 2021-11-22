"""get_ranges.

Реализовать функцию get_ranges которая получает на вход непустой
список неповторяющихся целых чисел, отсортированных по
возрастанию, которая этот список “сворачивает”
get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) // "0-4,7-8,10";
get_ranges([4,7,10]) // "4,7,10";
get_ranges([2, 3, 8, 9]) // "2-3,8-9";
"""

from typing import Any


class ArgumentError(Exception):
    """Exception to be raised when invalid arguments are passed into a function."""


def validate_input(arg: Any) -> bool:
    """Return True if argument passed is a list of non-negative integers."""
    if isinstance(arg, list) and arg:
        if not all(isinstance(x, int) and x > 0 for x in arg):
            return False
    else:
        return False
    return True


def get_ranges(input_list: list[int]) -> str:
    """Return a list of natural numbers to a string of ranges.

    Example:
    -------
        get_ranges([1, 2, 3, 7, 8, 12]) -> '1-3,7-8,12'

    """
    if not validate_input(input_list):
        raise ArgumentError('Expected a list of non-negative integers.')

    ranges = []
    input_iter = iter(set(sorted(input_list)))  # sort and remove duplicates
    left = right = next(input_iter)
    for cur in input_iter:
        if cur - right == 1:
            right = cur
        else:
            ranges.append((left, right))
            left = right = cur
    ranges.append((left, right))

    range_str = ','.join(
        list(
            map(
                lambda pair: f'{pair[0]}-{pair[1]}' if pair[0] < pair[1] else str(pair[0]),
                ranges
            )
        )
    )

    print(f'Ranges of {input_list}:\n{range_str!r}')
    return range_str
