"""Посчитать количество строчных (маленьких) и прописных (больших) букв в введенной строке.

Учитывать только английские буквы.

Оформите указанную задачу из прошлых домашних в виде функции и покройте
тестами. Учтите, что в функцию могут быть переданы некорректные значения,
здесь может пригодится ‘assertRaises’. Не нужно переделывать функцию для
того чтобы она ловила все возможные ситуации сама.
"""

import string

def get_count_by_case(input_str: str) -> tuple[int, int]:
    """Print the number of lowercase and uppercase alphabetic characters in a string."""
    lower_count, upper_count = (0, 0)
    for char in input_str:
        if char in string.ascii_letters:
            if char.islower():
                lower_count += 1
            else:
                upper_count += 1
    print(f'Lowercase count: {lower_count}. Uppercase count: {upper_count}')
    return lower_count, upper_count
