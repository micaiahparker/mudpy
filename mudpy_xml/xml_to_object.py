import xml.etree.ElementTree as ET

known = {}


def add_item(item):
    known[item.tag] = item


def add_items(*args):
    for item in args:
        known[item.tag] = item


def make_item(element):
    return known[element.tag](element)


def parse_xml(xml):
    root = ET.parse(xml).getroot()
    return make_item(root)


def get_contents(element):
    return [make_item(child) for child in element]


def get_bool(string):
    if string == "True" or string == "true":
        return True
    elif string == "False" or string == 'false':
        return False
    else:
        raise TypeError("Should be 'true' or 'false'")
