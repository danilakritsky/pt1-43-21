"""
List practice.

1. Используйте генератор списков чтобы получить следующий: ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
2. Используйте на предыдущий список slice чтобы получить следующий: ['ab', 'ad', 'bc'].
3. Используйте генератор списков чтобы получить следующий ['1a', '2a', '3a', '4a'].
4. Одной строкой удалите элемент '2a'; из прошлого списка и напечатайте его.
5. Скопируйте список и добавьте в него элемент '2a'; так чтобы в исходном списке этого
элемента не было.
"""


def main() -> None:
    """Perform list transformations according to the task instructions."""
    print(orig_ls := [a + b for a in 'ab' for b in 'bcd'])
    print(orig_ls[::2])
    print(orig_ls := [str(num) + 'a' for num in range(1, 5)])
    print(popped := orig_ls.pop(1))
    copy_ls = orig_ls.copy()
    copy_ls.insert(1, popped)
    print(copy_ls)
    print(orig_ls)


if __name__ == '__main__':
    main()
