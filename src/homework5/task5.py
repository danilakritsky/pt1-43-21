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


from collections import Counter
from collections import namedtuple

from task2 import prompt_until_match


def main() -> None:
    """Prompt user for student count and languages each student know.

    Print the languages known by all the students, followed by languages at least one student knows.
    """
    UserInput = namedtuple('UserInput', ['student_count', 'student_lang_count', 'lang'])
    prompt = UserInput(
        'Enter the number of students (>= 1):\n',
        'Enter the number of languages student {} knows (>= 1):\n',
        'Enter language {} (use double quotes to enter compounds):\n'
    )

    failed_msg = UserInput(
        'Please, provide an integer greater than 1!'.upper(),
        'Please, provide an integer greater than 1!'.upper(),
        'Please, provide a valid language name!'.upper(),
    )

    patterns = UserInput(
        pos_int := r'^(?!^[0]$)\d+$',
        pos_int,
        r"^(\"\w.*?\w\"|\w[-\w']+)$"
    )

    student_count = int(
        prompt_until_match(
            patterns.student_count,
            prompt.student_count,
            failed_msg.student_count,
        )[0]
    )

    students_langs = []
    for student in range(1, student_count + 1):
        student_lang_count = int(
            prompt_until_match(
                patterns.student_lang_count,
                prompt.student_lang_count.format(student),
                failed_msg.student_lang_count,
            )[0]
        )

        cur_stud_langs = []
        for lang_num in range(1, student_lang_count + 1):
            lang = prompt_until_match(
                patterns.lang,
                prompt.lang.format(lang_num),
                failed_msg.lang)[0]
            cur_stud_langs.append(lang)
        students_langs.extend(list(set(cur_stud_langs)))  # remove duplicates

    langs_count = Counter(students_langs)
    print('Languages all the students know:')
    for lang, count in langs_count.copy().items():
        if count == student_count:
            print(lang)
            langs_count.pop(lang)

    print(
        'Languages only some students know:',
        *(langs_count.keys() if langs_count.keys() else ('None',)),
        sep='\n')


if __name__ == '__main__':
    main()
