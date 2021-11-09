"""Слова.

Во входной строке записан текст. Словом считается последовательность непробельных
символов идущих подряд, слова разделены одним или большим числом пробелов или
символами конца строки. Определите, сколько различных слов содержится в этом тексте.
"""


from collections import namedtuple


def main() -> None:
    """Count the number of unqiue words in the input text.

    A word is a sequence of non-whitespace elements. Words are separated by one or more
    whitespace characters.
    """
    Prompt = namedtuple('Prompt', ['initial', 'continued'])
    prompt = Prompt(
        'Enter your text (pass an empty string to finish input):\n',
        'Enter line {} (pass an empty string to finish input):\n'
    )
    lines: list[str] = []
    while line := input(prompt.continued.format(len(lines) + 1) if lines else prompt.initial):
        lines.append(line)
    text = '\n'.join(lines)
    if not text:
        raise SystemExit('No text has been input.')
    print(f'This text contains {len(set(text.split()))} unique words.')


if __name__ == '__main__':
    main()
