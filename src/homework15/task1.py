"""Задача 1.

Создайте модель из жизни. Это может быть бронирование комнаты в отеле,
покупка билета в транспортной компании, или простая РПГ. Создайте
несколько объектов классов, которые описывают ситуацию. Объекты должны
содержать как атрибуты так и методы класса для симуляции различных
действий. Программа должна инстанцировать объекты и эмулировать какую-
либо ситуацию - вызывать методы, взаимодействие объектов и т.д.
"""


import datetime
import re


# pylint: disable=R0903
class Singleton(type):
    """Class representing a singleton pattern."""

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """Call the class."""
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class NotebookApp(metaclass=Singleton):
    """A class representing a note-taking app."""

    def __init__(self):
        """Initialize the instance object."""
        self._register = NoteRegister()
        self._trash = TrashBin()


class NoteRegister(metaclass=Singleton):
    """A class that stores notes."""

    def __init__(self):
        """Initialize the instance object."""
        self._register = {}

    @property
    def max_id(self):
        """Return the current max id in the register."""
        return max(self._register.keys()) if self._register else 0

    def register(self, task):
        """Add task to the register."""
        self._register[self.max_id + 1] = task


class TrashBin(metaclass=Singleton):
    """A class that stores deleted notes."""

    def __init__(self):
        """Initialize the instance object."""
        self._trash = {}

    def restore(self, note):
        """Restore a note from trash."""

    def remove(self, note):
        """Remove a note from trash."""

    def empty(self):
        """Empty the trash bin."""


class Note:
    """A class representing a note."""

    def __init__(self, body):
        """Initialize the instance object."""
        self.body = body
        self.created = datetime.datetime.now()

    def __repr__(self):
        """Return the string representation of the instance."""
        return (
            f'created: {self.created:%Y-%m-%d %H:%M:%S}\n'
            f'{self.body}\n'
        )

    def __str__(self):
        """Return the string representation of the instance."""
        return (
            f'created: {self.created:%Y-%m-%d %H:%M:%S}\n'
            f'{self.body}\n'
        )


class HelpString:
    """A class representing information about the apps options."""

    def __init__(self, flag, function, description):
        """Initialize the instance object."""
        self.flag = flag
        self.function = function
        self.description = description


class AppController(metaclass=Singleton):
    """A class representing the UI that passes commands to the app."""

    def __init__(self):
        """Initialize the instance object."""
        self._command_list = {
            '-h': FlagInfo('help', "Provides help about the app's options."),
            '-q': FlagInfo('quit', 'Exits the app.'),
            '-a': FlagInfo('add', 'Adds new note.'),
            '-d': FlagInfo('delete', 'Delete a note with the given id')
        }
        self.run()

    def run(self):
        """Run the app prompting user for input."""
        while (user_input := input('Input command (use -h for help):\n')).strip() != '-q':
            flag = user_input[:2]
            if flag == '-h':
                self.help()
            else:
                if flag in self._command_list and len(user_input) > 2:
                    parsed = self.parse_input(user_input)[0]
                    if parsed[0] in self._command_list:
                        flag, _ = parsed
                        self.__getattribute__(self._command_list[flag].function)()
                else:
                    print('flag not recognized')
                    continue

    def help(self):
        """Get help about the available options."""
        for flag, info in self._command_list.items():
            print(f'{flag}: {info.description}')

    @staticmethod
    def parse_input(user_input):
        """Parse input to extract flag and info."""
        regex = re.compile(r"^(-[hra]) (.*)$")
        match = re.findall(regex, user_input)
        return match


class FlagInfo:
    """A class representing information about the apps options."""

    def __init__(self, function, description):
        """Initialize the instance object."""
        self.function = function
        self.description = description


if __name__ == '__main__':
    AppController()
