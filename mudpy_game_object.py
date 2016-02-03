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

main_game = MudPyGameObject()
