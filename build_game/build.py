from inspect import isclass, getmembers
from sys import modules


def get_keys(xml):
    return xml.attrib.keys()


class Test:
    tag = 'test'


class Build:
    tag = 'build'
    build_from = [__name__]
    known = {}

    def __init__(self, xml):
        self.name = ""
        self.build_xml(xml)

    def get_keys(self):
        return self.__dict__.keys()

    def set_value(self, key, xml):
        self.__dict__[key] = xml.attrib[key]

    def update(self):
        for module in self.build_from:
            for name, cls in getmembers(modules[module], isclass):
                if cls.tag not in self.known:
                    self.known[cls.tag] = cls

    def build_xml(self, xml):
        for attr in get_keys(xml):
            if attr in self.get_keys():
                self.set_value(attr, xml)

if __name__ == "__main__":
    from xml.etree.ElementTree import fromstring

    Build(fromstring('<build name="Bob"/>')).update()
