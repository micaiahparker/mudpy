class Buildable(type):
    def __new__(mcs, *args, **kwargs):
        return super().__new__(mcs, *args, **kwargs)


class Build(metaclass=Buildable):
    tag = 'build'
    known = {}

    def __init__(self, xml):
        self.name = ""
        self.desc = ""
        self.contents = {}
        self.build(xml)

    def get_keys(self):
        return self.__dict__.keys()

    def set_value(self, key, value):
        self.__setattr__(key, value)

    def build(self, xml):
        for attr in xml.attrib:
            if attr in self.get_keys():
                self.set_value(attr, xml.attrib[attr])

        for child in xml:
            if child.tag in self.known.keys():
                self.add_item(child)

    def add_item(self, item):
        if item.tag in self.known:
            content = self.make_item(item)
            self.contents[content.name] = content

    def make_item(self, item):
        return self.known[item.tag](item)

    def get_id(self):
        return [word.lower() for word in self.name.split(' ') + self.desc.split(' ')]

    def id_score(self, *tags):
        count = 0
        for tag in tags:
            count += self.get_id().count(tag.lower())
        return count








