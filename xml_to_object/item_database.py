from xml_to_object.build_xml import *


class Rooms(Buildable):
    def __init__(self, xml):
        self.rooms = {}
        super().__init__(xml)

    def post_init(self):
        for content in self.contents:
            if content.tag == 'room':
                self.rooms[content.name] = content
                self.contents.remove(content)

    def get_room(self, name):
        try:
            return self.rooms[name]
        except KeyError:
            return None


class Room(Buildable):
    def __init__(self, xml):
        self.players = {}
        self.items = {}
        super().__init__(xml)

    def post__init__(self):
        for content in self.contents:
            if content.tag == 'player':
                self.players[content.name] = content
                self.contents.remove(content)
            elif content.tag == 'item':
                self.items[content.name] = content
                self.contents.remove(content)

    def look(self):
        return super().look(self.players, self.items)



