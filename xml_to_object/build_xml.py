known = {}


def add_known(cls):
    known[cls.tag] = cls


class Buildable:
    tag = 'buildable'

    def __init__(self, xml):
        self.contents = {}
        name = ""

        for key in self.__dict__:
            if key in xml.attrib:
                setattr(self, key, xml.attrib[key])

        self.post_init()

    def post_init(self):
        pass

