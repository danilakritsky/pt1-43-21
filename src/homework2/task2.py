"""
Найти самое длинное слово в введенном предложении.

Учтите что в предложении есть знаки препинания.
Подсказки:
- my_string.split([chars]) возвращает список строк.
- len(list) - количество элементов в списке
"""

import string


def main() -> None:
    """Return the longest word in a sentence."""
    while True:
        if (sentence := input('Please, enter your sentence:\n')):
            break
    # skip the hyphen ('-') for composite words like 'it-academy'
    trans_mapping = {ord(char): None for char in string.punctuation if char != '-'}
    word_list = sentence.translate(trans_mapping).split()
    print(max(word_list, key=len))


if __name__ == '__main__':
    main()
