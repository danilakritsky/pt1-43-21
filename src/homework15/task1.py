"""CLI based note-taking app.

class AppShell - main app interface that registers user input.
class CommandParser - object that parsed user input for commands.
class CommandDispatcher - dispatches recognized commands.
class NoteDatabase - stores notes.
class Note - a class representing a note.

class StdoutFormatter - adds formatting (font, background) to output.
"""


import datetime
import functools
import re
from collections import Counter
from typing import Callable


class StdoutFormatter:
    """A class comprising methods used to format output string using ASCII escape codes."""

    ESC = '\x1B'  # ANSI escape (\u001b)
    CSI = f'{ESC}['  # Control Sequence Introducer
    RESET = f'{CSI}0m'
    COLOR_CODES_3_BIT = {
        'black': 0,
        'red': 1,
        'green': 2,
        'yellow': 3,
        'blue': 4,
        'magenta': 5,
        'cyan': 6,
        'white': 7
    }

    GRAPHICS_MODES = {
        'bold': 1,
        'dim': 2,
        'italic': 3,
        'underline': 4,
        'strikethrough': 9
    }
    # make mode code available by using abbreviations
    GRAPHICS_MODES |= {key[0]: value for key, value in GRAPHICS_MODES.items()}

    FONT_SPECIFIER = '3'
    BACKGROUND_SPECIFIER = '4'
    COLOR_CODE_8_BIT = '8;5;{}'
    COLOR_CODE_24_BIT = '8;2;{};{};{}'

    @classmethod
    def prep_color_code(cls, *args) -> str:
        """Prepare a ANSI color code from values specified."""
        color_code = ''
        if not args:
            return color_code
        if len(args) == 1:
            color = args[0]
            if isinstance(color, int):
                if color < 0 or color > 255:
                    raise ValueError('No color with code {color}.')
                color_code = cls.COLOR_CODE_8_BIT.format(color)
            elif isinstance(color, str):
                color_code = str(cls.COLOR_CODES_3_BIT.get(color, 'not found'))
                if color_code == 'not found':
                    raise ValueError(f'{color!r} is not recognized.')
        elif len(args) == 3:
            if any(not isinstance(value, int) for value in args):
                raise ValueError('Expected a tuple of 3 integers.')
            if any(value < 0 or value > 255 for value in args):
                raise ValueError('Must specify a value in the range [0, 255].')
            color_code = cls.COLOR_CODE_24_BIT.format(*args)
        else:
            raise TypeError('Expected either int, str or 3 ints.')
        return color_code

    @classmethod
    def prep_graphics_code(cls, *args: str) -> str:
        """Prepare an ANSI graphics code from modes specified."""
        graphics_code = ''
        code_arr: str | tuple[str, ...]
        if not args:
            return graphics_code
        if len(args) == 1:
            code_arr = args[0]
            if not isinstance(code_arr, str):
                raise ValueError('Expected a string of code abbreviations.')
        else:
            code_arr = args
        modes: list[str] = []
        for mode in code_arr:
            if not isinstance(mode, str):
                raise ValueError('Expected str.')
            if (mode_recognized := cls.GRAPHICS_MODES.get(mode, '')):
                modes.append(str(mode_recognized))
        graphics_code = ';'.join(modes)
        return graphics_code

    @classmethod
    def format_string(cls, *graphics_mode_args) -> Callable:
        """Create a function that can be used to format a string."""
        def font(*font_code_args):
            def background(*background_code_args):
                graphics_mode = cls.prep_graphics_code(*graphics_mode_args)
                font_color = cls.prep_color_code(*font_code_args)
                background_color = cls.prep_color_code(*background_code_args)
                if font_color:
                    font_color = cls.FONT_SPECIFIER + font_color
                if background_color:
                    background_color = cls.BACKGROUND_SPECIFIER + background_color
                format_str = (
                    cls.CSI
                    + graphics_mode  # noqa: W503
                    + (';' if graphics_mode and (font_color or background_color) else '')  # noqa: W503
                    + font_color  # noqa: W503
                    + (';' if (font_color and background_color) else '')  # noqa: W503
                    + background_color  # noqa: W503
                    + 'm'  # noqa: W503
                )
                return lambda x: format_str + x + cls.RESET
            return background
        return font

class CommandParser:
    """A class that parses commands from the shell and forwards them to the dispatcher to be executed."""

    APP_COMMANDS = {
        '-h': 'help',
        '-n': 'new_note',
        '-t': 'title',
        '-#': 'tag',
        '-ct': 'color_tag',
        '-e': 'edit',
        '-d': 'delete',
        '-r': 'restore',
        '-discard': 'discard',
        '-empty': 'empty',
        '-quit': 'quit',
        '-save': 'save',
        '-load': 'load',
    }

    @staticmethod
    def _identify_commands(command: str) -> list[tuple[str, ...]]:
        """Parse the user input."""
        pattern = re.compile(
            r"""
                # use only the space character classes to match whitespace with re.VERBOSE
            (?:(?<=^)|(?<=\s))  # either start of the line or a whitespace
            (-[hntedr]|-[#]|-ct|-quit|-discard|-empty|-save|-load)  # FLAG (any of the commands)
            (?:
                (?=()$)  # end of the line
                |
                (?:
                    \s+(?!(?:-[hntedr]|-[#]|-ct|-quit|-discard|-empty|-save|-load))  # space not followed by flag
                    (.*?)  # some text
                    (?:
                        (?=\s(?:-[hntedr]|-[#]|-ct|-quit|-discard|-empty|-save|-load)(?:\s|$))  # another flag followed by either whitespace or end of line
                        |
                        (?=$)  # end of the line
                    )
                )  
                |
                (?=\s+(?:-[hntedr]|-[#]|-ct|-quit|-discard|-empty|-save|-load)())  # whitespace and another flag
            )  # either whitespace or end of line
            """,
        re.VERBOSE)
        return re.findall(pattern, command)

    @staticmethod
    def _clear_commands(commands: list[tuple[str, ...]]) -> list[tuple[str, str]]:
        """Remove unnecessary capture groups."""
        flags, operands = [], []
        for command_tup in commands:
            flag = command_tup[0]
            operand = ''.join(command_tup[1:])
            flags.append(flag)
            operands.append(operand)
        return list(zip(flags, operands))

    @classmethod
    def _validate_commands(cls, commands: list[tuple[str, str]]) -> list[tuple[str, str]] | str:
        """Validate if commands can be send to be executed."""
        if not commands:
            return f'No command could be recognized.'
        flags, _ = zip(*commands)
        command_count = Counter(flags)
        cannot_be_combined = [
            '-h', '-n', '-e', '-d', '-r', '-quit', '-discard', '-empty', '-save', '-load'
        ]
        no_operand_needed = ['-h', '-quit', '-empty']
        operand_needed = cls.APP_COMMANDS.keys() - no_operand_needed
        requires_another_command = ['-t', '-#', '-ct']
        bold_blue = StdoutFormatter.format_string('b')('blue')()
        if sum(int(flag in cannot_be_combined) for flag in flags) > 1:
            return f'Flags {bold_blue(", ".join(cannot_be_combined))} cannot be combined or repeated.'
        for command, key in commands:
            if command in no_operand_needed and key:
                return f'Flags {bold_blue(", ".join(no_operand_needed))} don\'t take operands.'
            if command in operand_needed and not key:
                return f'Flags {bold_blue(", ".join(operand_needed))} require operands.'
            if command in requires_another_command and not ({'-n', '-e'} & set(flags)):
                return f'Flags {bold_blue(", ".join(requires_another_command))} can only be used together with "-e" or "-n".'
            if command != '-#' and command_count[command] > 1:
                return f'Only {bold_blue("-#")} flag can be used more than once in a single command statement.'
        return commands

    @classmethod
    def prepare_commands(cls, command: str) -> list[tuple[str, str]] | str:
        """Prepare commands before dispatching them."""
        cmd_to_dispatch = functools.reduce(lambda x, y: y(x), [
            command,
            cls._identify_commands,
            cls._clear_commands,
            cls._validate_commands
            ])
        return cmd_to_dispatch

class Note:
    """A class representing a note."""
    def __init__(self, text: str, title: str = 'Untitled'):
        self.id = None
        self.text = text
        self.title = title
        self.tags = set()
        self.color_tag = None
        self.deleted = False
        self.created = datetime.datetime.now()

    def __str__(self):
        """Return the string representation of the instance."""
        bold = StdoutFormatter.format_string('b')()()
        italic = StdoutFormatter.format_string('i')()()
        blue = StdoutFormatter.format_string()('blue')()
        italic_dim = StdoutFormatter.format_string('di')(245)()
        italic_dim_blue = StdoutFormatter.format_string('id')('blue')()
        italic_dim_red = StdoutFormatter.format_string('id')('red')()
        red = StdoutFormatter.format_string('')('red')()
        return (
            '---\n'
            + (f'{self.color_tag}{chr(32)}' if self.color_tag else '')
            + f'{bold(self.title)}\n'
            + italic(f'{self.text}\n')
            + italic_dim(f'created: {self.created:%Y-%m-%d %H:%M:%S}\n')
            + italic_dim_blue(f'tags:{chr(32)}')
            + (blue(f'{", ".join(self.tags)}') if self.tags else italic_dim_blue("None")) + '\n'
            + italic_dim_red(f'id:{chr(32)}')
            + (red(f'{self.id}') if self.id else italic_dim_red("None")) + '\n'
            + '---'
        )

class NoteDatabase:
    """A class representing the database containing all notes."""
    database = {}

    @classmethod
    def generate_id(cls) -> int:
        """Generate a numeric id for a note."""
        return max(cls.database.keys()) + 1 if cls.database.keys() else 1

    @classmethod
    def get_note(cls, note_id: int) -> Note:
        """Retrieve a note with the given id from NoteDatabase."""
        return cls.database.get(note_id, 'No note with the specified id.')

    @classmethod
    def register_note(cls, note: Note) -> None:
        """Add note to a database."""
        note_id = cls.generate_id()
        note.id = note_id
        cls.database[note_id] = note
    
    @classmethod
    def delete_note(cls, note_id: int) -> None:
        """Delete note."""
        if isinstance(note:= cls.get_note(note_id), Note):
            cls.database[note_id].deleted = True
        else:
            print(note)
    
    @classmethod
    def restore_note(cls, note_id: int) -> None:
        """Restore note."""
        if isinstance(note:= cls.get_note(note_id), Note):
            if note.deleted == True:
                note.deleted = False
            else:
                print('Cannot restore: note is not the trash.')
        else:
            print(note)
        
    @classmethod
    def discard_note(cls, note_id: int) -> None:
        """Discard a note removing it from the database."""
        if isinstance(note:= cls.get_note(note_id), Note):
            if note.deleted == True:
                del cls.database[note_id]
            else:
                print('Can only discard deleted notes.')
        else:
            print(note)
    
    @classmethod
    def empty_trash(cls, note_id: int) -> None:
        """Discard all deleted note from the database."""
        for id, note in cls.database:
            if note.deleted == True:
                del cls.database[id]
    
class CommandDispatcher:
    """Class that prepare and dispatches commands."""

    COMMAND_MAPPING = {
        '-h': 'help',
        '-n': 'new_note',
        '-#': 'add_tag',
        '-ct': 'add_color_tag',
        '-t': 'add_title',
        '-d': 'delete_note',
        '-e': 'edit_note',
        '-r': 'restore_note',
        '-empty': 'empty_trash',
        '-discard': 'discard_note',
        '-quit': 'quit',
        '-save': 'save_notes',
        '-load': 'load_notes'
    }


    @classmethod
    @staticmethod
    def order_commands(command_list: list[tuple[str, str]]):
        """Orders commands before dispatching."""
        command_list.sort(key=lambda x: 0 if x[0] in ('-e', '-n') else 1)
        return command_list

    @classmethod
    @staticmethod
    def help(cls):
        bold_green = StdoutFormatter.format_string('b')('green')()
        print(cls)
        for key, value in cls.COMMAND_MAPPING.items():
            print(f'{bold_green(key)} -- {value}')

    @staticmethod
    def new_note(text: str) -> Note:
        """Create a new note."""
        note =  Note(text)
        NoteDatabase.register_note(note)
        return note
    
    @classmethod
    @staticmethod
    def edit_note(note_id: str):
        """Return a note to edit."""
        return NoteDatabase.get_note(int(note_id))

    @staticmethod
    def add_tag(note: Note, tag: str) -> Note:
        """Add tag to a note."""
        note.tags.add(tag)

    @staticmethod
    def add_title(note: Note, title: str) -> Note:
        """Add title to a note."""
        note.title = title

    @staticmethod
    def add_color_tag(note: Note, color: str) -> Note:
        """Add color tag to a note."""
        note.color_tag = StdoutFormatter.format_string()(color)()('\u25A0')

    @classmethod
    @staticmethod
    def dispatch(cls, command_list: list[tuple[str, str]]):
        """Dispatches commands."""
        first_command = command_list[0]
        flag, operand = first_command
        func_name = cls.COMMAND_MAPPING[flag]
        res = cls.__dict__[func_name].__func__(operand)
        if isinstance(res, Note):  # continue if a Note instance has been returned
            if (more_commands := command_list[1:]):
                for command, inner_operand in more_commands:
                    print(command, inner_operand)
                    func_name = cls.COMMAND_MAPPING[command]
                    cls.__dict__[func_name].__func__(res, inner_operand)

class AppShell:
    """The main interface for the app - regisers user commands."""

    command_log = {}

    @classmethod
    @staticmethod
    def run(cls):
        """Run the app prompting user for input."""
        
        light_blue_background_blue_font = StdoutFormatter.format_string()('blue')(240, 255, 255)
        blue_font =  StdoutFormatter.format_string()(50, 150, 200)()
        prompt = (
            light_blue_background_blue_font(f'Input command (use -h for help):') + '\n'
            + f'{blue_font(">>> ")}'
        )
        while (user_input := input(prompt).strip()) != '-quit':
            if user_input == '-h':
                CommandDispatcher.help(CommandDispatcher)
                continue
            commands = CommandParser.prepare_commands(user_input)
            if isinstance(commands, list):
                cls.log_command(commands)
                CommandDispatcher.dispatch(CommandDispatcher, commands)
            else:
                print(commands)
            cls.notes_view()

    @classmethod
    def log_command(cls, command: str) -> None:
        """Log command storing it along with its execution datetime stamp."""
        cls.command_log[f'{datetime.datetime.now():%Y-%m-%d %H:%M:%S}'] = command


    @staticmethod
    def notes_view():
        for note in NoteDatabase.database.values():
            print(note)

if __name__ == '__main__':
    AppShell.run(AppShell)
