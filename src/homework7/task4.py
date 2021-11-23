"""Двоичная пирамида.

На вход функции передаются два целых числа m и n, такие что 0 ≤ m ≤ n.
Функция выполняет следующие действия:
a. Перевести числа от m до n (включительно) в двоичные числа.
b. Сложить полученные двоичные числа по основанию 10.
c. Перевести результат сложения в двоичную число.
d. Вернуть строку с результатом.
Пример:
func(1, 4) --> 1111010
1 // 1 в двоичном виде 1
+ 10 // 2 в двоичном виде 10
+ 11 // 3 в двоичном виде 11
+ 100 // 4 в двоичном виде 100
-----
122 // 122 в двоичном виде 1111010
"""


def sum_of_bin_repr(start: int, end: int) -> str:
    """Return the sum of binary representations of each number in the range from start to end."""
    if not all(isinstance(arg, int) for arg in (start, end)):
        raise TypeError('Function accepts only integers.')
    if any(arg < 0 for arg in (start, end)):
        raise ValueError('Only positive integers are allowed.')
    if end < start:
        raise ValueError('end should be greater than or equal to start.')

    total = 0
    for num in range(start, end + 1):
        total += int(f'{num:b}')
    print(f'Sum of binary representations of numbers from {start} to {end} in binary:\n{total:b}')
    return f'{total:b}'
