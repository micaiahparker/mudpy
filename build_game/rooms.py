from build_game import build
from build_game import items


class Room(build.Build):
    tag = 'room'
    containers = {'chests': 'chest',
                  'npcs': 'npc',
                  'rooms': 'room'}
    players = []
    build_from = [__name__]


class Chest(build.Build):
    tag = 'chest'
    containers = {'inventory': 'item'}
    build_from = [items.__name__]

    def __init__(self, xml):
        self.locked = False
        super().__init__(xml)


class NPC(build.Build):
    tag = 'npc'
    containers = {'inventory': 'item'}
    build_from = [items.__name__]



