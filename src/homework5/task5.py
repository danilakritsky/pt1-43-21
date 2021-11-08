"""Языки.

Каждый из N школьников некоторой школы знает Mi языков. Определите, какие языки знают
все школьники и языки, которые знает хотя бы один из школьников.
Входные данные
Первая строка входных данных содержит количество школьников N. Далее идет N чисел Mi,
после каждого из чисел идет Mi строк, содержащих названия языков, которые знает i-й
школьник.

Пример входных данных:
3 # N количество школьников
2 # M1 количество языков первого школьника
Russian # языки первого школьника
English
3 # M2 количество языков второго школьника
Russian
Belarusian
English
3
Russian
Italian
French
"""


from collections import namedtuple
import re


def main() -> None:
    """Doc!!!!!!!"""
    Prompt = namedtuple('Prompt', ['student_count', 'student_lang_count', 'lang'])
    prompt = Prompt(
        'Enter the number of students (>= 1):\n',
        'Enter the number of languages student {} knows:\n',
        'Enter language:\n'
    )
    pos_int_pattern = '^(?!^[0]$)\d+$'
    while not (num_match := re.search(pos_int_pattern, input(prompt.student_count))):
        continue
    student_count = int(num_match[0])
    
    all_students_langs = []
    for student in student_count:
        while not (num_match := re.search(pos_int_pattern, input(prompt.student_count))):
            continue
        student_lang_count = int(num_match[0])
        student_langs = []
        while 


if __name__ == '__main__':
    main()