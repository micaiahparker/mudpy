from xml.etree.ElementTree import parse
from game.command import Command
from game.ingame.world import World


class MudpyGame:
    def __init__(self, file):
        self.world = World(parse(file))
        self.players = {}

    def send(self, player_id, line):
        self.world.send(Command(self.players[player_id], self.world, line))

    def add_player(self, player):
        self.players[player.id] = player

    def remove_player(self, player_id):
        del self.players[player_id]
