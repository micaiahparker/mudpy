from inspect import isclass, getmembers
from sys import modules


def get_keys(xml):
    return xml.attrib.keys()


class Build:
    tag = 'build'
    build_from = [__name__]
    known = {}

    def __init__(self, xml):
        self.name = ""
        self.contents = {}
        self.update_known()
        self.set_attrib(xml)
        self.set_children(xml)

    def get_keys(self):
        return self.__dict__.keys()

    def set_key(self, key, xml):
        self.__dict__[key] = xml.attrib[key]

    def make_item(self, xml):
        if xml.tag in self.known:
            return self.known[xml.tag](xml)

    def update_known(self):
        for module in self.build_from:
            for name, cls in getmembers(modules[module], isclass):
                if cls.tag not in self.known:
                    self.known[cls.tag] = cls

    def set_attrib(self, xml):
        for attr in get_keys(xml):
            if attr in self.get_keys():
                self.set_key(attr, xml)

    def set_children(self, xml):
        for child in xml:
            if child.tag in self.known:
                self.contents[child.attrib['name']] = self.make_item(child)


class Test(Build):
    tag = 'test'

    def __init__(self, xml):
        self.test_var = 0
        super().__init__(xml)
