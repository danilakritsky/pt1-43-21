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


from collections import Counter, namedtuple
import re


def get_positive_int(prompt: str) -> int:
    """Prompt user until he inputs a positive integer."""
    while not (pos_int_match := re.search(r'^(?!^[0]$)\d+$', input(prompt))):
        continue
    return int(pos_int_match[0])


def get_word(prompt: str) -> str:
    """Prompt user for input until he inputs a non-empty alhpabetic word.

    Compounds can be input if enclosed in double quotes (e.g. "Costa Rica").
    """
    while not (match := re.search(r"^(\"\w.*?\w\"|\w[-\w']+)$", input(prompt))):
        continue
    return match[0]


def main() -> None:
    """Prompt user for student count and languages each student know.

    Print the languages known by all the students, followed by languages at least one student knows.
    """
    Prompt = namedtuple('Prompt', ['student_count', 'student_lang_count', 'lang'])
    prompt = Prompt(
        'Enter the number of students (>= 1):\n',
        'Enter the number of languages the student {} knows (>= 1):\n',
        'Enter language {} (use double quotes to enter compounds):\n'
    )
    student_count = get_positive_int(prompt.student_count)

    students_langs = []
    for student in range(student_count):
        student_lang_count = get_positive_int(prompt.student_lang_count.format(student + 1))
        cur_stud_langs = []
        for lang_num in range(student_lang_count):
            lang = get_word(prompt.lang.format(lang_num + 1))
            cur_stud_langs.append(lang)
        students_langs.extend(list(set(cur_stud_langs)))  # remove duplicates

    langs_count = Counter(students_langs)
    print('Languages all the students know:')
    for lang, count in langs_count.copy().items():
        if count == student_count:
            print(lang)
            langs_count.pop(lang)
    print('Languages only some students know:')
    for lang, count in langs_count.items():
        print(lang)


if __name__ == '__main__':
    main()
