import asyncio
from mudpy_game_object import main_game as game


class MudPyProtocol(asyncio.Protocol):
    def __init__(self):
        self.transport = None

    def connection_made(self, transport):
        self.transport = transport
        game.add_player(self)

    def connection_lost(self, exc):
        game.remove_player(self)

    def data_received(self, data):
        game.send_all(self, data)

    def send(self, data):
        self.transport.write(data)






