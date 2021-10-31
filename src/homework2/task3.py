"""Вводится строка. Требуется удалить из нее повторяющиеся символы и все пробелы.
Например, если было введено "abc cde def", то должно быть выведено "abcdef".
"""


def main() -> None:
    """Strip all repeating characters and whitespace from a string
    and print the result."""
    while True:
        if (input_str := input('Enter a string:\n')):
            break
    # creating a dict from a string will both preserve the order and remove duplicates
    # using a dict comprehension as an alternative to dict.fromkeys()
    # to filter out whitespace in a single statement
    char_dict = {char: None for char in input_str if not char.isspace()}
    print(''.join(char_dict.keys()))


if __name__ == '__main__':
    main()
