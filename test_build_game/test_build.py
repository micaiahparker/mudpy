from build_game.build import Build
from xml.etree.ElementTree import parse

test_xml = parse("test.xml").getroot()


def test_build_init():
    """test build init"""
    assert Build(test_xml)


def test_build_tag():
    """test build tag"""
    assert Build(test_xml).tag == 'build'


def test_build_name():
    """test build name"""
    assert Build(test_xml).name == ""
