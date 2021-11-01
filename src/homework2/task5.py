"""
Выведите n-ое число Фибоначчи, используя только временные переменные,
циклические операторы и условные операторы. n - вводится
"""


def main() -> None:
    """Print the nth fibonacci number."""
    while True:
        user_input = input('Enter a positive integer:\n')
        if user_input.isdigit() and ((num_to_find := int(user_input)) > 0):
            break
    first, second = (0, 1)
    if num_to_find == 1:
        num = first
    elif num_to_find == 2:
        num = second
    else:
        cur_count = 2
        while cur_count < num_to_find:
            num = first + second
            first, second = second, num
            cur_count += 1
    print(num)


if __name__ == '__main__':
    main()
