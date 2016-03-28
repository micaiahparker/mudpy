class Build:
    tag = 'build'
    known = {}

    def __init__(self, xml):
        self.name = ""
        self.desc = ""
        self.contents = {}
        self.build(xml)

    def build(self, xml):
        for tag in self.known.keys():
            self.contents[tag] = {}

        for attr in xml.attrib:
            if attr in vars(self).keys():
                setattr(self, attr, xml.attrib[attr])

        for child in xml:
            if child.tag in self.known.keys():
                self.add_item(child)
            else:
                raise BuildUnknownException(obj=self.tag, item=child.tag)

    def add_item(self, item):
        new_item = self.make_item(item)
        if new_item.name == "" or new_item.desc == "":
            raise BuildNoNameException(tag=new_item.tag)
        self.contents[new_item.tag][new_item.name] = new_item

    def make_item(self, item):
        return self.known[item.tag](item)


class BuildUnknownException(BaseException):
    def __init__(self, *args, obj, item, **kwargs):
        print("{} cannot build item {}.".format(obj, item))
        super().__init__(*args, **kwargs)


class BuildNoNameException(BaseException):
    def __init__(self, *args, tag, **kwargs):
        print("Attempted to build item {} with no name or desc", format(tag))
        super().__init__(*args, **kwargs)
