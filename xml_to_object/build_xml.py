known = {}


def add_known(*args):
    for cls in args:
        known[cls.tag] = cls


def make_item(item):
    if item.tag in known:
        return known[item.tag](known)
    return None


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


