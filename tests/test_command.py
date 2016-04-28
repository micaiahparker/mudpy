from game.command import *


def test_command():
    class Test(Commandable):
        @command
        def test(self):
            return True

    assert Test().has_command('test')
