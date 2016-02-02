from mudpy_xml.xml_to_object import *


class Object:
    def __init__(self, element):
        self.model = element.attrib['model']
        self.name = element.attrib['name']

    def __str__(self):
        return self.name


class Container(Object):
    tag = "container"

    def __init__(self, element):
        super().__init__(element)
        self.locked = get_bool(element.attrib['locked'])
        self.contents = get_contents(element)

    def print_contents(self):
        ret = "\n"
        for content in self.contents:
            ret += content
        return ret + "\n"

    def __str__(self):
        return "{}: {}".format(self.name, self.print_contents())

    def is_locked(self):
        return self.locked


def load_objects():
    add_item(Container)
