"""Задача 1.

Создайте модель из жизни. Это может быть бронирование комнаты в отеле,
покупка билета в транспортной компании, или простая РПГ. Создайте
несколько объектов классов, которые описывают ситуацию. Объекты должны
содержать как атрибуты так и методы класса для симуляции различных
действий. Программа должна инстанцировать объекты и эмулировать какую-
либо ситуацию - вызывать методы, взаимодействие объектов и т.д.
"""
class Task:
    def __init__(self, descr, due_date):
        self.description = descr
        self.due_date = due_date
        self.completed = False

    def __repr__(self):
        return f'{self.due_date} | {self.description}'
    def __str__(self):
        return f'{self.due_date} | {self.description}'


class TaskList:
    def __init__(self):
        self.task_list = set()

    def __repr__(self):
        for task in self.task_list:
            print(task)

    def __str__(self):
        str_repr = ''
        for task in self.task_list:
            str_repr += str(task) + '\n'
        return str_repr

    def __iadd__(self, other):
        if isinstance(other, Task):
            self.task_list.add(other)
        return self

            

lst = TaskList()
lst += Task('Todo 1', '2021-02-01')
lst += Task('Todo 2', '2021-03-01')
print(lst)