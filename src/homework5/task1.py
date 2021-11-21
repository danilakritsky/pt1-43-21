"""Dict comprehensions.

Создайте словарь с помощью генератора словарей, так чтобы его ключами были числа от 1 до
20, а значениями кубы этих чисел.
"""


def main() -> dict:
    """Create a dict via a dict comprehension.

    Keys are numbers from 1 to 20, values are cubes of its keys.
    """
    return {num: num ** 3 for num in range(1, 21)}
