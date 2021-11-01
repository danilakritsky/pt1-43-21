"""Зарегистрируйтесь на одном (или нескольких) из сайтов:
https://py.checkio.org/ , https://www.codewars.com, https://www.hackerrank.com/,
https://acmp.ru И решите 1-5 задач уровня Elementary и advanced. Поместите 3 простых
и 2 сложных задачи на Ваш выбор в пул реквест."""


from string import ascii_lowercase


def square_sum(numbers: list[int]) -> int:
    """Complete the square sum function so that it squares each number
    passed into it and then sums the results together.
    For example, for [1, 2, 2] it should return 9 because 1^2 + 2^2 + 2^2 = 9.
    @ https://www.codewars.com/kata/515e271a311df0350d00000f/train/python/
    """
    return sum([num ** 2 for num in numbers])


def descending_order(num: int) -> int:
    """Your task is to make a function that can take any non-negative integer as an argument
    and return it with its digits in descending order. Essentially, rearrange the digits
    to create the highest possible number.
    Examples:
    Input: 42145 Output: 54421
    Input: 145263 Output: 654321
    Input: 123456789 Output: 987654321
    @ https://www.codewars.com/kata/5467e4d82edf8bbf40000155/train/python
    """
    if num < 0:
        raise SystemExit("Only positive integers are allowed.")
    return int(''.join(sorted(str(num), reverse=True)))


def is_isogram(string: str) -> bool:
    """
    An isogram is a word that has no repeating letters, consecutive or non-consecutive.
    Implement a function that determines whether a string that contains only letters
    is an isogram. Assume the empty string is an isogram. Ignore letter case.
    "Dermatoglyphics" --> true
    "aba" --> false
    "moOse" --> false (ignore letter casing)
    @ https://www.codewars.com/kata/54ba84be607a92aa900000f1/train/python/
    """
    string = string.lower()
    return (len(set(string)) == len(string))


def sum_pairs(ints: list[int], sum_to_match: int) -> list[int]:
    """
    Given a list of integers and a single sum value, return the first two values
    (parse from the left please) in order of appearance that add up to form the sum.

    sum_pairs([11, 3, 7, 5],         10)
    #              ^--^      3 + 7 = 10
    == [3, 7]

    sum_pairs([4, 3, 2, 3, 4],         6)
    #          ^-----^         4 + 2 = 6, indices: 0, 2 *
    #             ^-----^      3 + 3 = 6, indices: 1, 3
    #                ^-----^   2 + 4 = 6, indices: 2, 4
    #  * entire pair is earlier, and therefore is the correct answer
    == [4, 2]

    sum_pairs([0, 0, -2, 3], 2)
    #  there are no pairs of values that can be added to produce 2.
    == None/nil/undefined (Based on the language)

    sum_pairs([10, 5, 2, 3, 7, 5],         10)
    #              ^-----------^   5 + 5 = 10, indices: 1, 5
    #                    ^--^      3 + 7 = 10, indices: 3, 4 *
    #  * entire pair is earlier, and therefore is the correct answer
    == [3, 7]
    Negative numbers and duplicate numbers can and will appear.

    NOTE: There will also be lists tested of lengths upwards of 10,000,000 elements.
    Be sure your code doesn't time out.
    @ https://www.codewars.com/kata/54d81488b981293527000c8f/train/python/
    """

    lefts = set()  # a set of all left elements of a potential pair
    for num in ints:
        # we have a pair if there is a number left in lefts such that left + num == s
        if (left := sum_to_match - num) in lefts:
            return [left, num]
        lefts.add(num)
    raise SystemExit('No valid pair has been found.')


def alphabet_position(text: str) -> str:
    """
    In this kata you are required to, given a string,
    replace every letter with its position in the alphabet.
    If anything in the text isn't a letter, ignore it and don't return it.
    "a" = 1, "b" = 2, etc.
    Example:
    alphabet_position("The sunset sets at twelve o' clock.")
    Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"
    (as a string)
    @ https://www.codewars.com/kata/546f922b54af40e1e90001da/train/python/
    """
    alphabetized = []
    for letter in text.lower():
        if letter.isalpha():
            alphabetized.append(
                str(ascii_lowercase.index(letter) + 1)
            )
    return ' '.join(alphabetized)
