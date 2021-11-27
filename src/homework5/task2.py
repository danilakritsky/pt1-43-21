"""Города.

Дан список стран и городов каждой страны. Затем даны названия городов.
Для каждого города укажите, в какой стране он находится.

Входные данные
Программа получает на вход количество стран N. Далее идет N строк, каждая строка начинается
с названия страны, затем идут названия городов этой страны.
В следующей строке записано число M, далее идут M запросов — названия каких-то M городов,
перечисленных выше.
Выходные данные
Для каждого из запроса выведите название страны, в котором находится данный город.
Примеры

Входные данные
2
Russia Moscow Petersburg Novgorod Kaluga
Ukraine Kiev Donetsk Odessa

3
Odessa
Moscow
Novgorod

Выходные данные
Ukraine
Russia
Russia
"""


from collections import namedtuple
import re


UserInputs = namedtuple('UserInputs', ['country_num', 'city_list', 'city_num', 'city'])


def set_up() -> tuple[UserInputs, ...]:
    """Return the user input variables for the main function to use."""
    prompt = UserInputs(
        'Enter the number of countries (>= 2):\n> ',
        ('Enter the name for the country number {} followed by its cities (at least 1) '
            'separated by space\n'
            '(use double quotes to specify composite names like \"New York\"):\n> '),
        'Enter the number of cities to search:\n> ',
        'Enter the name of the city number {}:\n> '
    )
    fail_msg = UserInputs(
        'Please, provide a positive number greater than 1!'.upper(),
        'Please, provide a valid country name followed by at least one of its cities!'.upper(),
        'Please, provide a positive number!'.upper(),
        'Please provide a valid city name!'.upper()
    )
    pattern = UserInputs(
        r'^(?!^[01]$)\d+$',  # integer greater than 1
        location_pattern := re.compile(
            r"""(
            \"\w.*?\w\"    # multi word names like "St. Louis", must be passed in double quotes!
            |
            \w[-\w']+      # single word names, accounted for names like Санкт-Петербург, O'Fallon
            )
            """,
            re.VERBOSE
        ),
        r'^(?!^[0]$)\d+$',  # positive integer
        location_pattern
    )

    return prompt, fail_msg, pattern


def prompt_until_match(regex: str, prompt: str, failed_msg: str) -> list[str]:
    """Prompt user for input until it matches a regular expression."""
    while not (match := re.findall(regex, input(prompt))):
        print(failed_msg)
        continue
    return match


def store_data() -> dict:
    """Prompt user for consecutive inputs of country names followed by its cities."""
    prompt, fail_msg, pattern = set_up()

    # get the country count
    country_count = (
        int(prompt_until_match(
            pattern.country_num,
            prompt.country_num,
            fail_msg.country_num)[0]
            )
    )

    # get cities
    locations_dict = {}
    for country_num in range(1, country_count + 1):
        # prompt until at least one city is input
        while True:
            match = prompt_until_match(
                pattern.city_list,
                prompt.city_list.format(country_num),
                fail_msg.city_list)
            if len(match) >= 2:
                break
            print('Please, provide at least one country and one city!'.upper())
        country, *cities = match
        locations_dict.update({city: country for city in cities})

    return locations_dict


def query_data(locations_dict: dict) -> None:
    """Prompt the user for city names and return the country the city belongs to."""
    prompt, fail_msg, pattern = set_up()
    # get the city count
    city_count = (
        int(prompt_until_match(
            pattern.city_num,
            prompt.city_num,
            fail_msg.city_num)[0]
            )
    )

    # get city names
    for city_num in range(1, city_count + 1):
        city_match = prompt_until_match(
            pattern.city,
            prompt.city.format(city_num),
            fail_msg.city)
        print(locations_dict.get(city_match[0], 'City not found.'))


if __name__ == '__main__':
    query_data(store_data())
