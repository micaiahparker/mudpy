import asyncio
from mudpy_protocol import MudPyProtocol


class MudPyServer:
    def __init__(self, port):
        self.loop = asyncio.get_event_loop()
        self.server = self.loop.create_server(MudPyProtocol, port=port)

    def start(self):
        self.loop.run_until_complete(self.server)
        try:
            self.loop.run_forever()
        except KeyboardInterrupt:
            self.stop()

    def stop(self):
        if self.loop.is_running():
            self.loop.call_soon_threadsafe(self.loop.stop)
