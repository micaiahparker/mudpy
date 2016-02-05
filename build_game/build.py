from inspect import isclass, getmembers
from sys import modules


def get_keys(xml):
    return xml.attrib.keys()


class Build:
    tag = 'build'
    build_from = [__name__]
    known = {}
    containers = {}

    def __init__(self, xml):
        self.name = ""
        self.contents = []
        self.update_known()
        self.set_attrib(xml)
        self.set_children(xml)
        self.sort_containers()

    def get_keys(self):
        return self.__dict__.keys()

    def set_key_from_xml(self, key, xml):
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
                self.set_key_from_xml(attr, xml)

    def set_children(self, xml):
        for child in xml:
            if child.tag in self.known:
                self.contents.append(self.make_item(child))

    def sort_containers(self):
        for content in self.contents:
            for container in self.containers:
                if content.tag == self.containers[container]:
                    self.add_to_container(container, content)

    def add_to_container(self, container, item):
        if container not in self.__dict__.keys():
            self.__dict__[container] = {}
        self.__dict__[container][item.name] = item


class Test(Build):
    tag = 'test'

    def __init__(self, xml):
        self.test_var = 0
        super().__init__(xml)
