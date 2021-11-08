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
    while (remainder := first % second) != 0:
        first, second = second, remainder
    return second


def test_gcd_euclid():
    """Test the gcd_euclid() function."""
    test_data = (
        (0, 0, 0),
        (0, 100, 100),
        (7, 13, 1),
        (5, 10, 5),
        (8, 8, 8)
    )
    for first, second, expected in test_data:
        assert (output := gcd_euclid(first, second)) == expected, (
            f'Expected {expected}, got {output}.'
        )
    print('Tests passed.')


if __name__ == '__main__':
    test_gcd_euclid()