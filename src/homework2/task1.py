"""Напишите программу, которая считает общую цену. Вводится M рублей и N копеек
цена, а также количество S товара Посчитайте общую цену в рублях и копейках за L
товаров.
Пример:
Input: Цена одной вещи 3 рубля 20 копеек, посчитать 3 предмета.
Output: Общая цена 9 рублей 60 копеек"""


def get_input(prompt: str) -> int:
    """Prompt user for a non-negative integer and return it."""
    while True:
        user_input = input(prompt)
        if user_input.isdigit():
            return int(user_input)
        print('Please, provide a non-negative integer!')


def main() -> None:
    """Print the total cost of an item given its price and quantity."""
    prompts = [
        "Enter the ruble part of the item's price:\n",
        "Enter the copeck part of the item's price:\n",
        "Enter the item quantity:\n"
    ]
    rubles, copecks, qty = [get_input(prompt) for prompt in prompts]
    total = (rubles * 100 + copecks) * qty
    print(f'Your total is {total // 100} rubles and {total % 100} copecks.')


if __name__ == '__main__':
    main()
