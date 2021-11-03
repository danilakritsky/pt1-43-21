"""List practice.

1. Используйте генератор списков чтобы получить следующий: ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
2. Используйте на предыдущий список slice чтобы получить следующий: ['ab', 'ad', 'bc'].
3. Используйте генератор списков чтобы получить следующий ['1a', '2a', '3a', '4a'].
4. Одной строкой удалите элемент '2a'; из прошлого списка и напечатайте его.
5. Скопируйте список и добавьте в него элемент '2a'; так чтобы в исходном списке этого
элемента не было.
"""


def main() -> None:
    """Perform list transformations according to the task instructions."""
    orig_ls = [a + b for a in 'ab' for b in 'bcd']
    assert orig_ls == ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'], (
        "Expected ['ab', 'ac', 'ad', 'bb', 'bc', 'bd']."
    )
    assert orig_ls[::2] == ['ab', 'ad', 'bc'], "Expected ['ab', 'ad', 'bc']."

    orig_ls = [str(num) + 'a' for num in range(1, 5)]
    assert orig_ls == ['1a', '2a', '3a', '4a'], "Expected ['1a', '2a', '3a', '4a']."

    print(popped := orig_ls.pop(1))
    copy_ls = orig_ls.copy()
    copy_ls.insert(1, popped)
    assert copy_ls == ['1a', '2a', '3a', '4a'], "Expected ['1a', '2a', '3a', '4a']."
    assert orig_ls == ['1a', '3a', '4a'], "Expected ['1a', '3a', '4a']."


if __name__ == '__main__':
    main()
