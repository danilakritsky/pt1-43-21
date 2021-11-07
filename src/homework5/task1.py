"""Dict comprehensions.

Создайте словарь с помощью генератора словарей, так чтобы его ключами были числа от 1 до
20, а значениями кубы этих чисел.
"""


def main() -> None:
    """Create a dict via a dict comprehension.

    Keys are numbers from 1 to 20, values are cubes of its keys.
    """
    dict_ = {num: num ** 3 for num in range(1, 21)}
    assert isinstance(dict_, dict), 'Wrong type!'
    assert list(dict_.keys()) == (nums := list(range(1, 21))), 'Wrong keys!'
    assert list(dict_.values()) == list(map(lambda x: pow(x, 3), nums)), 'Wrong values!'
    print('Tests passed.')


if __name__ == '__main__':
    main()
