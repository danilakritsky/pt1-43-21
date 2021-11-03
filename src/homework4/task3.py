"""
Tuple practice.

Создайте кортеж из одного элемента, чтобы при итерировании по этому элементу
последовательно выводились значения 1, 2, 3. Убедитесь что len() исходного кортежа
возвращает 1.
"""


def main() -> None:
    """
    Create a 1-tuple.

    Iterating through the tuple's single element should yied 1, 2, 3.
    """
    tup = ([1, 2, 3], )
    assert all(a == b for a, b in zip(tup[0], [1, 2, 3])), 'Wrong element!'
    assert len(tup) == 1, 'Expected 1.'
    print('Tests passed.')


if __name__ == '__main__':
    main()
