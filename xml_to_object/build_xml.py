known = {}


def add_known(*args):
    for cls in args:
        known[cls.tag] = cls


def make_item(item):
    if item.tag in known:
        return known[item.tag](known)
    return None


def list_dict(adict):
    ret = "\n"
    for arg in adict:
        ret += "{}\n".format(str(arg))

    return ret


def content_rules(inst, content):
    if content.tag in known:
        content = make_item(content)
        try:
            inst.__dict__[content.tag][content.name] = content
        except KeyError:
            inst.__dict__[content.tag] = {}
            inst.__dict__[content.tag][content.name] = content


class Buildable:
    tag = 'buildable'
    viewables = []

    def __init__(self, xml):
        self.contents = []
        self.name = ""

        for key in self.__dict__:
            if key in xml.attrib:
                setattr(self, key, xml.attrib[key])

        for child in xml:
            content_rules(self, child)

        self.post_init()

    def post_init(self):
        pass

    def examine(self):
        ret = ""

        for key in self.__dict__.keys():
            if key in self.viewables or 'all' in self.viewables:
                ret += list_dict(self.__dict__[key])

        return ret

    def __str__(self):
        return self.name + self.examine()

add_known(Buildable)

