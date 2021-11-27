"""Даны два списка чисел.

Посчитайте, сколько различных чисел содержится одновременно как в первом списке, так и во втором.
"""


def intersection_count(first_list: list[int], second_list: list[int]) -> int:
    """Return the count of unique numbers that are present in both supplied lists."""
    for input_list in (first_list, second_list):
        if not (isinstance(input_list, list) and all(isinstance(elem, int) for elem in input_list)):
            raise TypeError('Expected list of ints.')

    unique_count = len(set(first_list) & set(second_list))
    print(f'Count of unique items: {unique_count}')
    return unique_count
