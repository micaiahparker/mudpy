from xml_to_object.item_database import *


class Buildable:
    tag = 'buildable'

    def __init__(self, xml):
        self.contents = []
        self.name = ""

        for key in self.__dict__:
            if key in xml.attrib:
                setattr(self, key, xml.attrib[key])

        for child in xml:
            self.contents.append(make_item(child))

        self.post_init()

    def post_init(self):
        pass

add_known(Buildable)


