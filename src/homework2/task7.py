"""Даны: три стороны треугольника. Требуется: проверить, действительно ли это
стороны треугольника. Если стороны определяют треугольник, найти его площадь.
Если нет, вывести сообщение о неверных данных."""


def get_positive_int(prompt: str) -> int:
    """Prompt user for a positive integer and return it."""
    while True:
        user_input = input(prompt)
        if user_input.isdigit() and ((num := int(user_input)) > 0):
            return num
        print('Please, provide a positive integer!')


def main() -> None:
    """Prompt the user for three sides of a triangle and compute the area
    of the triangle if valid side lengths have been provided."""
    template = 'Enter the length of the {side_num} side:\n'
    prompts = ['first', 'second', 'third']
    sides = [
        get_positive_int(template.format(side_num=prompt)) for prompt in prompts
    ]

    # test for triangle inequality
    perimeter = sum(sides)
    for side in sides:
        if perimeter - side <= side:
            raise SystemExit('Invalid side lengths.')

    # find the area using the Heron's formula
    # √(s(s - a)(s - b)(s - c)) == √(s - 0) * √(s - a) * √(s - c) * √(s - c)
    area = 1.0
    for i in ([0] + sides):
        area *= (perimeter / 2 - i) ** (1 / 2)
    print(area)


if __name__ == '__main__':
    main()
