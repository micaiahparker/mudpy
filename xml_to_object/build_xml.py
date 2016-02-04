known = {}


class Buildable:
    tag = 'buildable'

    def __init__(self, xml):
        self.contents = {}
        for key in self.__dict__:
            if key in xml.attrib:
                setattr(self, key, xml.attrib[key])
        for child in xml:
            if child.tag in known:
                try:
                    self.contents[child.tag][child.attrib['name']] = known[child.tag](child)
                except KeyError:
                    self.contents[child.tag] = {}
                    self.contents[child.tag][child.attrib['name']] = known[child.tag](child)
