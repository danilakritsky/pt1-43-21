"""Числа.

Даны два натуральных числа. Вычислите их наибольший общий делитель при помощи
алгоритма Евклида (мы не знаем функции и рекурсию).
"""


def gcd_euclid(first: int, second: int) -> int:
    """Return the greatest common denominator of 2 natural numbers using the Euclidean algorithm.

    0 is considered natural.
    """
    if 0 in (pair := (first, second)):  # additionally handles the (0, 0) case
        return max(pair)
    if first < second:
        first, second = second, first
    while (remainder := first % second):
        first, second = second, remainder
    print(f'GCD of {pair[0]} and {pair[1]} is {second}.')
    return second
