"""Оформите решение задач из прошлых домашних работ в функции.

Напишите функцию runner. (все станет проще когда мы изучим модули,
getattr и setattr)
a. runner() – все фукнции вызываются по очереди
b. runner(‘func_name’) – вызывается только функцию func_name.
c. runner(‘func’, ‘func1’...) - вызывает все переданные функции
"""


MODULE_NAMES = ('homework2', 'homework4', 'homework5')


# pylint: disable = R0903
class FakeModule():
    """A class faking a module."""


# pylint: disable = W0511
# TODO: create a function factory
def set_up() -> None:
    """Set up the global namespace."""
    for module in MODULE_NAMES:
        globals()[module] = FakeModule()
        func_names = []
        for func_num in range(1, 8):
            # pylint: disable = W0122
            exec(f'def func{func_num}():\n print("Called func{func_num}.")\n', globals())
            func_names.append(f'func{func_num}')
        for name in func_names:
            if name.startswith('func'):
                setattr(globals()[module], name, globals().pop(name))


# TODO: refactor to remove duplication
def runner(*args: str) -> None:
    """Run each function in the passed as an argument."""
    mod_message = 'From {}:'
    if not args:
        for modname in MODULE_NAMES:
            for func in (attrs := globals()[modname].__dict__):
                print(mod_message.format(modname))
                attrs[func]()
    else:
        for func in args:
            for modname in MODULE_NAMES:
                if func in (attrs := globals()[modname].__dict__):
                    print(mod_message.format(modname))
                    attrs[func]()


if __name__ == '__main__':
    set_up()
    runner()
    runner('func1')
    runner('func1', 'func2', 'func3')
