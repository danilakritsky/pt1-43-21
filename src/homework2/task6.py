"""Определите, является ли число палиндромом (читается слева направо и справа
налево одинаково). Число положительное целое, произвольной длины. Задача
требует работать только с числами (без конвертации числа в строку или что-нибудь
еще)"""


def main() -> None:
    """Check whether a number is a palindrome."""
    while True:
        user_input = input('Enter a positive integer:\n')
        if user_input.isdigit() and ((num := int(user_input)) > 0):
            break
    orig_num = num
    reversed_num = 0
    while num > 0:
        last_digit = num % 10
        # append the digit to the end of the reversed number
        reversed_num = reversed_num * 10 + last_digit
        num = num // 10
    print(orig_num == reversed_num)


if __name__ == '__main__':
    main()
