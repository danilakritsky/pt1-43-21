"""Задача 2.

Создайте декоратор, который вызывает задекорированную функцию пока она
не выполнится без исключений (но не более n раз - параметр декоратора). Если
превышено количество попыток, должно быть возбуждено исключение типа
TooManyErrors
"""

from typing import Any
from typing import Callable
from typing import Generator


class TooManyErrors(Exception):
    """Raise if a function has exceeded its call attempts limit."""


class FunctionWithCallAttemptsLimit:
    """A function that can be called only the specified number of times.

    If the function returns a value succesfully, this value will be returned on each following call.
    If the function uses all its attempts but fails to return a valid value,
    TooManyErrors Exception will be raised on each following call.
    """

    def __init__(self, func: Callable, call_limit: int) -> None:
        """Initialize the instance of FunctionWithCallAttemptsLimit."""
        self.func_name: str = func.__name__
        self.call_limit: int = call_limit
        self.call_count: int = 0
        self.finished: bool = False
        self.failed: bool = False
        self.result: Any = None
        # original function is converted to a generator to support send(), throw() and close()
        self.__func_as_gen: Generator[None, None | tuple[tuple, dict], None] = self.caller(func)
        self.__func_as_gen.send(None)  # initialize the generator

    def __repr__(self) -> str:
        """Return the representation of an instance."""
        cls_name: str = type(self).__name__
        func_name: str = self.func_name
        address: str = hex(id(self))
        state: str
        if self.finished:
            state = f'finished (result={self.result})'
        elif self.failed:
            state = 'failed'
        else:
            state = f'not finished (attempts_left={self.attempts_left})'
        repr_str: str = (
            f"<{cls_name} object at {address},"
            f"\n\tfunc: {func_name},"
            f"\n\tstate: {state}>")
        return repr_str

    def caller(self, func: Callable):
        """Call a function with arguments provided via the send() method."""
        while True:
            args, kwargs = yield
            try:
                self.result = func(*args, **kwargs)
            except Exception as error:  # pylint: disable=W0703
                self.result = error

    @property
    def attempts_left(self) -> int:
        """List the number of call attempts left."""
        return self.call_limit - self.call_count

    def register_call(self) -> Any:
        """Register the last call to a function before returning the result."""
        self.call_count += 1
        if isinstance(self.result, Exception):
            if self.attempts_left:
                affix = (
                    '' if self.attempts_left % 10 == 1 and self.attempts_left % 100 != 11 else 's'
                )
                print(f'Exception occured:\n{self.result!r}\n'
                      f'{self.attempts_left} attempt{affix} left.')
                return self.result
            self.__func_as_gen.close()  # close the generator so that no more calls can be made
            self.failed = True
            print('Function failed.')
            return self.result
        self.__func_as_gen.close()
        self.finished = True
        print('Call succeeded.')
        return self.result

    def __call__(self, *args, **kwargs) -> Any:
        """Call the function with the given arguments."""
        if self.finished:
            print(f'Function has already returned a valid value.\n'
                  f'Result: {self.result}')
            return self.result
        if self.failed:
            self.__func_as_gen.throw(TooManyErrors)
            return None
        self.__func_as_gen.send((args, kwargs))
        return self.register_call()


def limit_calls(limit):
    """Restrict the number of function calls to a specified limit."""
    def decorator(func):
        return FunctionWithCallAttemptsLimit(func, limit)
    return decorator
