import sys
import inspect


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
        self.contents[item.tag].append(self.make_item(item))

    def make_item(self, item):
        return self.known[item.tag](item)

    def get_class_members(self):
        return inspect.getmembers(sys.modules[self.__module__], inspect.isclass)


class BuildException(BaseException):
    def __init__(self, *args, obj, item, **kwargs):
        print("{} cannot build item {}.".format(obj, item))
        super().__init__(*args, **kwargs)




