"""Задача со звездочкой.

Реализовать функцию, на вход которой передается имя логической функции
(т.е. функция, которая принимает логические параметры и возвращает
логическое значение. Пример: И, ИЛИ, исключающее ИЛИ и т.д.) и набор
аргументов, и возвращает строку, представляющую таблицу истинности
функции.
Пример ввода: some_func("AND", A, B)
Правила форматирования:
● Переменные должны называться A, B, C, D ... и так далее, в том же
порядке, в котором они передаются в логическую функцию.
● Параметров не будет больше 26 (A ... Z)
● Логические значения будут представлены либо 1 (истина), либо 0 (ложь).
Первая строка будет состоять из следующих частей:
● имена переменных, разделенные пробелом ()
● два символа табуляции
● имя функции, параметры которой в круглых скобках разделены запятыми
● два символа новой строки
Следующие строки будут состоять из следующих по порядку:
● значения переменных, разделенные пробелом
● два символа табуляции
● результат функции для этого расположения переменных
● символ новой строки
"""

from itertools import product
from typing import Any


def name_params(*args: Any) -> list[str]:
    """Assign name (a letter from A to Z) to each argument and return these names as a list."""
    if len(args) > 26:
        raise TypeError('name_params() can not take more than 26 arguments.')
    names = []
    for num, _ in enumerate(args):
        names.append(chr(65 + num))
    return names


def logic_gate(oper, *args: Any) -> int:
    """Simulate a logic gate's output with arguments used as input."""
    operations = {
        'NOT': lambda x: not x[0],
        'AND': all,
        'OR': any,
        # karnaugh map
        'XOR': lambda x: any(y ^ z for y, z in zip(x[:-1], x[1:])),
        'NAND': lambda x: not all(x),
        'NOR': lambda x: not any(x),
        'XNOR': lambda x: all(args) or not any(args)
    }
    if oper not in operations:
        raise SystemExit(f'Operation {oper!r} is not recognized.')
    if oper == 'NOT':
        if len(args) == 1:
            return int(operations[oper](args))
        raise TypeError(f'Only one operand is allowed for{oper!r}.')
    if len(args) == 1:
        raise TypeError(f'{oper!r} requires at least 2 operands.')
    return int(operations[oper](args))


def truth_table(oper: str, *args: Any) -> None:
    """Print truth table for a given number of arguments."""
    names = name_params(*args)
    signature = (f'{oper}({",".join(names)})')  # add opertion signature
    combinations = list(product([0, 1], repeat=len(args)))
    results = []
    for comb in combinations:
        results.append(logic_gate(oper, *comb))
    print(*names, end='\t' * 2)
    print(signature)
    for comb, res in zip(combinations, results):
        print(*comb, end='\t' * 2)
        print(res)
