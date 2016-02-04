from server.mudpy_parsers import *


class MudPyGameObject:
    def __init__(self):
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def remove_player(self, player):
        self.players.remove(player)

    def send_all(self, player, data):
        for p in self.players:
            if p is not player:
                p.send(data)

    def get_data(self, player, data):
        command = parse_data(data)
        self.parse_command(player, command)

    def parse_command(self, player, command):
        pass

main_game = MudPyGameObject()
