"""Упорядоченный список.

Дан список целых чисел. Требуется переместить все ненулевые элементы в левую
часть списка, не меняя их порядок, а все нули - в правую часть. Порядок ненулевых
элементов изменять нельзя, дополнительный список использовать нельзя, задачу
нужно выполнить за один проход по списку. Распечатайте полученный список.
"""


def move_zeros(lst: list):
    """Move all zeroes to the right side of the list."""
    no_zeros = [el for el in lst if el != 0]
    return no_zeros + [0] * (len(lst) - len(no_zeros))


def test_move_zeros():
    """Run assertions on the move_zeros functions."""
    test_cases: list[tuple] = [
        ([], []),
        ([1, 2, 3, 0, 3, 0, 1, 1], [1, 2, 3, 3, 1, 1, 0, 0]),
        ([1, -1], [1, -1])
    ]

    for test_data, expected in test_cases:
        orig_lst = test_data.copy()
        res = move_zeros(test_data)
        assert res == expected, f'Expected {expected}, got {res}.'
        print(f'Sorting {orig_lst}:\n{test_data}\n')


if __name__ == '__main__':
    test_move_zeros()
