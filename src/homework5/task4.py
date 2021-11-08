"""Даны два списка чисел.

Посчитайте, сколько различных чисел входит только в один из этих списков
"""


from collections import namedtuple


def difference_count(first_list: list[int], second_list: list[int]) -> tuple[int, int]:
    """For 2 input lists return the count of unique numbers present only in this list as a tuple."""
    first_set, second_set = (set(lst) for lst in (first_list, second_list))
    return len(first_set - second_set), len(second_set - first_set)


def test_difference_count() -> None:
    """Test the difference_count() function."""
    first_list = list(range(1, 11))
    second_lists, expected = zip(
        (first_list, (0, 0)),
        (list(range(6, 16)), (5, 5)),
        (list(range(1, 16)), (0, 5)),
        (list(range(1, 6)), (5, 0))
    )

    TestCase = namedtuple(
        'TestCase',
        ['second_list', 'expected', 'first_list'],
        defaults=[first_list]
    )

    test_cases = [TestCase(*case) for case in zip(second_lists, expected)]

    for test_case in test_cases:
        output = difference_count(test_case.first_list, test_case.second_list)
        assert output == test_case.expected, f'Expected {test_case.expected}, got {output}.'
    print('Tests passed.')


if __name__ == '__main__':
    test_difference_count()
