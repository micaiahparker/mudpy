from inspect import getmembers, isfunction


def command(func):
    func.command = True
    return func


class Commandable:
    def __init__(self):
        self.commands = {}
        self.get_commands()

    def get_commands(self):
        for name, func in getmembers(self.__class__, isfunction):
            if getattr(func, 'command', False):
                self.commands[name] = func

    def has_command(self, name):
        if name in self.commands.keys():
            return True
        else:
            return False


