"""Даны два списка чисел.

Посчитайте, сколько различных чисел входит только в один из этих списков
"""


def difference_count(first_list: list[int], second_list: list[int]) -> tuple[int, int]:
    """Return the count of unique numbers in each list.

    Numbers present in both lists are excluded.
    """
    first_set, second_set = (set(lst) for lst in (first_list, second_list))
    unique_in_first, unique_in_second = len(first_set - second_set), len(second_set - first_set)
    print(
        f'Count of unique items in the first list: {unique_in_first}',
        f'Count of unique items in the second list: {unique_in_second}',
        sep='\n')
    return unique_in_first, unique_in_second
