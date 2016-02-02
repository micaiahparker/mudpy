from mudpy_xml.xml_to_object import *


class Buildable:
    def __init__(self, element):
        self.name = element.attrib['name']

    def __str__(self):
        return self.name


class Container(Buildable):
    tag = "container"

    def __init__(self, element):
        super().__init__(element)
        self.locked = get_bool(element.attrib['locked'])
        self.contents = get_contents(element)

    def print_contents(self):
        ret = "\n"
        for content in self.contents:
            ret += str(content)+'\n'
        return ret

    def __str__(self):
        return "{}: {}".format(self.name, self.print_contents())

    def is_locked(self):
        return self.locked


class Player(Buildable):
    tag = "player"

    def __init__(self, element):
        super().__init__(element)
        self.race = element.attrib['race']
        self.role = element.attrib['role']
        self.gender = element.attrib['gender']

    def __str__(self):
        return "{} is a {} {}.".format(self.name, self.race, self.role)


class Weapon(Buildable):
    tag = "weapon"

    def __init__(self, element):
        super().__init__(element)
        self.attack = element.attrib['attack']
        self.defense = element.attrib['defense']
        self.hands = element.attrib['hands']

    def __str__(self):
        return "{} does {} attack and {} defense. Requires {} hands.".format(self.name, self.attack,
                                                                             self.defense, self.hands)

def load_objects():
    add_items(Container, Player, Weapon)


