from xml_to_object import build_xml


class MudPyGame(build_xml.Buildable):
    tag = 'game'

    def __init__(self, xml):
        self.starting_room_name = ""
        self.starting_room = None
        super().__init__(xml)
        self.starting_room = self.contents['room'][self.starting_room_name]

    def add_player(self, player):
        self.starting_room.add_player(player)

    def remove_player(self, player):
        for room in self.contents['room']:
            room.remove(player)




