import asyncio
from system.clients import ClientHolder


class MUDProtocol(asyncio.Protocol):
    def connection_made(self, transport):
        self.transport = transport
        ClientHolder().add(self)

    def connection_lost(self, exc):
        ClientHolder().remove(self)

    def data_received(self, data):
        ClientHolder().send(data)


class MUDServer:
    def __init__(self, port):
        self.port = port
        self.loop = asyncio.get_event_loop()
        self.coro = self.loop.create_server(MUDProtocol, None, self.port)

    def start(self):
        self.loop.run_until_complete(self.coro)
        self.loop.run_forever()

    def stop(self):
        if self.loop.is_running():
            self.loop.call_soon_threadsafe(self.loop.stop)

if __name__ in "__main__":
    server = MUDServer(1234)
    server.start()


