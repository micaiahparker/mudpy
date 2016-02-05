def get_keys(xml):
    return xml.attrib.keys()


class Build:
    tag = 'build'

    def __init__(self, xml):
        self.name = ""
        self.build_xml(xml)

    def get_keys(self):
        return self.__dict__.keys()

    def set_value(self, key, xml):
        self.__dict__[key] = xml.attrib[key]

    def build_xml(self, xml):
        for attr in get_keys(xml):
            if attr in self.get_keys():
                self.set_value(attr, xml)




