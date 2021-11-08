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


def main():
    """Prompt user for consecutive inputs of country names followed by its cities.

    Then iteratively prompt the user for city names and return the country the city belongs to.
    """
    Prompt = namedtuple('Prompt', ['country_num', 'city_list', 'city_num', 'city'])
    prompt = Prompt(
        'Enter the number of countries (>= 2):\n',
        ('Enter a country name followed by its cities (at least 1) separated by space.\n'
            '(use double quotes to specify composite names like \"New York\"):\n'),
        'Enter the number of cities to search:\n',
        'Enter the city name:\n'
    )
    while not (num_match := re.search(r'^(?!^[01]$)\d+$', input(prompt.country_num))):
        continue
    country_count = int(num_match[0])

    location_pattern = re.compile(
        r"""(
            \"\w.*?\w\"    # multi word names like "St. Louis", must be passed in double quotes!
            |
            \w[-\w']+      # single word names, accounted for names like Санкт-Петербург, O'Fallon
            )
        """,
        re.VERBOSE
    )

    locations_dict = {}
    for _ in range(country_count):
        # prompt until at least one city is input
        while len(string_match := re.findall(location_pattern, input(prompt.city_list))) < 2:
            continue
        country, *cities = string_match
        locations_dict.update({city: country for city in cities})

    while not (num_match := re.search(r'^(?!^[0]$)\d+$', input(prompt.city_num))):
        continue
    city_count = int(num_match[0])

    city_pattern = r"^(\"\w.*?\w\"|\w[-\w']+)$"
    for _ in range(city_count):
        while not (city_match := re.match(city_pattern, input(prompt.city))):
            continue
        print(locations_dict.get(city_match[0], 'City not found.'))


if __name__ == '__main__':
    main()
