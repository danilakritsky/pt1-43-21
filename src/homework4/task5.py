"""
Уникальные элементы в списке.

Дан список. Выведите те его элементы, которые встречаются в списке только один
раз. Элементы нужно выводить в том порядке, в котором они встречаются в списке.
"""


def get_unique_elements(lst: list) -> list:
    """Given a list return only its unique elements preserving the order of appearance."""
    uniques = []
    for elem in lst:
        if elem not in uniques:
            uniques.append(elem)
            continue
        uniques.remove(elem)
    return uniques


def test_get_unique_elements() -> None:
    """Run assertions on the get_unique_elements function."""
    test_cases: list[tuple] = [
        ([], []),
        ([[1, 2], 'a', 'a', 'b'], [[1, 2], 'b']),
        ([1, 2, 'a', 4, 'a', 1], [2, 4])
    ]

    for test_data, expected in test_cases:
        res = get_unique_elements(test_data)
        assert res == expected, f'Expected {expected}, got {res}.'
        print(f'Unique elements of {test_data} are:')
        for elem in res:
            print(elem)


if __name__ == '__main__':
    test_get_unique_elements()
