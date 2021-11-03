"""FizzBuzz.

Напишите программу, которая печатает цифры от 1 до 100, но вместо чисел, кратных 3
пишет Fizz, вместо чисел кратный 5 пишет Buzz, а вместо чисел одновременно кратных и 3 и 5
- FizzBuzz
"""


def main() -> None:
    """Print numbers from 1 to 100.

    Print Fizz for multiples of three, Buzz for multiples of 5,
    print FizzBuzz for multiples of both three and five.
    """
    for num in range(1, 101):
        # multiples of 15 are multiples of both 3 and 5
        for divisor, sub in zip([15, 5, 3], ['FizzBuzz', 'Buzz', 'Fizz']):
            if num % divisor == 0:
                print(sub)
                break
        else:
            print(num)


if __name__ == '__main__':
    main()
