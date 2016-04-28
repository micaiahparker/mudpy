from game.build import Build
from game.command import Commandable, command


class GameObject(Build, Commandable):
    def __init__(self, xml):
        super().__init__(xml)





