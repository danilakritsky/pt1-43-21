"""
Посчитать количество строчных (маленьких) и прописных (больших) букв в введенной строке.

Учитывать только английские буквы.
"""


def main() -> None:
    """Print the number of lowercase and uppercase alphabetic characters in a string."""
    while True:
        if (input_str := input('Enter a string:\n')):
            break
    lower_count, upper_count = (0, 0)
    for char in input_str:
        if char.isalpha():
            if char.islower():
                lower_count += 1
            upper_count += 1
    print(f'Lowercase count: {lower_count}. Uppercase count: {upper_count}')


if __name__ == '__main__':
    main()
