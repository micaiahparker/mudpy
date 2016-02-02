from mudpy_items.items import *
from mudpy_xml.xml_to_object import *


def load_game():
    load_objects()
    print(parse_xml("sandbox.xml"))

if __name__ == "__main__":
    load_game()
