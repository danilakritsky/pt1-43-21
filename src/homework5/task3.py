"""Даны два списка чисел.

Посчитайте, сколько различных чисел содержится одновременно как в первом списке, так и во втором.
"""


from collections import namedtuple


def intersection_count(first_list: list[int], second_list: list[int]) -> int:
    """Return the count of unique numbers that are present in both supplied lists."""
    return len(set(first_list) & set(second_list))


def test_intersection_count() -> None:
    """Test the intersection_count() function."""
    first_list = list(range(1, 11))
    second_lists, expected = zip(
        ([], 0),
        (first_list[:5], 5),
        (first_list[-3:], 3),
        (first_list[::3], 4),
        (first_list * 3, 10)
    )

    TestCase = namedtuple(
        'TestCase',
        ['second_list', 'expected', 'first_list'],
        defaults=[first_list]
    )

    test_cases = [TestCase(*case) for case in zip(second_lists, expected)]

    for test_case in test_cases:
        output = intersection_count(test_case.first_list, test_case.second_list)
        assert output == test_case.expected, f'Expected {test_case.expected}, got {output}.'
    print('Tests passed.')


if __name__ == '__main__':
    test_intersection_count()
