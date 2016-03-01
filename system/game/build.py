class Build:
    tag = 'build'

    def __init__(self, xml):
        self.name = ""
        self.desc = ""
        self.build(xml)

    def get_keys(self):
        return self.__dict__.keys()

    def set(self, key, value):
        self.__setattr__(key, value)

    def build(self, xml):
        for attr in xml.attrib:
            if attr in self.get_keys():
                self.set(attr, xml.attrib[attr])

    def get_id(self):
        return [word.lower() for word in self.name.split(' ') + self.desc.split(' ')]

    def id_score(self, *tags):
        count = 0
        for tag in tags:
            count += self.get_id().count(tag.lower())
        return count









