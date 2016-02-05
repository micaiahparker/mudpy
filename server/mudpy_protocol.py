import asyncio


class MudPyProtocol(asyncio.Protocol):
    def __init__(self):
        self.transport = None

    def connection_made(self, transport):
        pass

    def connection_lost(self, exc):
        pass

    def data_received(self, data):
        pass

