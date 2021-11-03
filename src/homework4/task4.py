"""
Пары элементов.

Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
Считается, что любые два элемента, равные друг другу образуют одну пару,
которую необходимо посчитать.
Входные данные - строка из чисел, разделенная пробелами.
Выходные данные - количество пар.
Важно: 1 1 1 - это 3 пары, 1 1 1 1 - это 6 пар
"""

from collections import Counter
import string


def get_valid_input() -> list[int]:
    """Prompt user for input.

    If input contains a list of digits delimited by space return the list.
    """
    while True:
        input_str = input('Enter a space delimited list of positive integers:\n')
        if set(input_str).issubset(set(string.digits + ' ')):
            return [int(num) for num in input_str.split(' ')]


def main() -> None:
    """Count the number of pairs in a list of integers.

    A pair consists of two elements equal to each other.
    """
    int_list = get_valid_input()
    counter_dict = Counter(int_list)  # key - integer, value - integer count
    pairs = 0
    for value_count in counter_dict.values():
        if value_count > 1:
            # to get the number of pairs (without replacement) in the same-element array
            # we can iterate through the array,
            # counting the number of elements to the right of the current element
            # and adding them together
            # e.g. for [1, 1, 1, 1] we get 3 + 2 + 1 + 0 = 6
            # which is equal to summing up all numbers counting down from (len(array) - 1) to 1
            pairs += sum(range(value_count - 1, 0, -1))
    print(pairs)


if __name__ == '__main__':
    main()
