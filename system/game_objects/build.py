class Build:
    tag = 'build'
    known = {}

    def __init__(self, xml):
        self.name = ""
        self.desc = ""
        self.contents = {}
        self.build(xml)

    def build(self, xml):
        for attr in xml.attrib:
            if attr in vars(self).keys():
                setattr(self, attr, xml.attrib[attr])

        for child in xml:
            if child.tag in self.known.keys():
                self.add_item(child)
            else:
                raise BuildException(obj=self.tag, item=child.tag)

    def add_item(self, item):
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


class BuildException(BaseException):
    def __init__(self, *args, obj, item, **kwargs):
        print("{} cannot build item {}.".format(obj, item))
        super().__init__(*args, **kwargs)



