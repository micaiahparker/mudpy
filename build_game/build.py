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
        self.desc = ""
        self.update_known()
        self.set_attrib(xml)
        self.set_children(xml)
        self.sort_containers()

    def get_keys(self):
        return self.__dict__.keys()

    def set_key_from_xml(self, key, xml):
        self.__dict__[key] = self.process_attr(xml.attrib[key])

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

    def process_attr(self, attr):
        if attr == "true" or attr == "True":
            return True
        elif attr == "false" or attr == "False":
            return False
        else:
            return attr

    def set_children(self, xml):
        for child in xml:
            if child.tag in self.known:
                self.contents.append(self.make_item(child))

    def sort_containers(self):
        for content in self.contents:
            for container in self.containers:
                if content.tag == self.containers[container]:
                    self.add_to_container(container, content)

    def get_container(self, container):
        try:
            return self.__dict__[container]
        except KeyError:
            return {}

    def add_to_container(self, container, item):
        if container not in self.__dict__.keys():
            self.__dict__[container] = {}
        self.__dict__[container][item.name] = item

    def get_container_string(self, container):
        ret = ""
        for item in self.get_container(container):
            ret += "{}\n".format(str(item))
        return ret

    def get_all_containers_string(self):
        ret = ""
        for container in self.containers.keys():
            ret += self.get_container_string(container)
        return ret

    def update(self, message):
        print(message)

    def __str__(self):
        return "{}\n{}\n{}".format(self.name, self.desc, self.get_all_containers_string())


class Test(Build):
    tag = 'test'

    def __init__(self, xml):
        self.test_var = 0
        self.test_bool = False
        super().__init__(xml)
