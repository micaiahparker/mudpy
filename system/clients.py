from system.patterns.singleton import Singleton


class ClientHolder(metaclass=Singleton):
    def __init__(self):
        self.clients = {}

    def add(self, client):
        self.clients[client.name] = client

    def remove(self, client):
        del self.clients[client.name]

    def send(self, message):
        for client in self.clients:
            client.send(message)


class Client:
    def __init__(self, protocol):
        self.protocol = protocol
        self.name = self.get_peername()

    def get_peername(self):
        return self.protocol.transport.get_extra_info('peername')

    def send(self, message):
        self.protocol.transport.write(message)

