from xml.etree.ElementTree import fromstring, parse


class MudpyGameBuilder:
    def __init__(self, path):
        self.root = parse(path+"/defaults.xml").getroot()

