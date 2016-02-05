from build_game.build import Build
from xml.etree.ElementTree import fromstring
from nose.tools import *

test_xml = fromstring('<build name="test"/>')


def test_build_init():
    """test build init"""
    assert_true(Build(test_xml))


def test_build_tag():
    """test build tag"""
    assert_equals(Build(test_xml).tag, 'build')


def test_build_name():
    """test build name"""
    assert_equals(Build(test_xml).name, "test")


def test_should_fail():
    """should fail"""
    assert_raises(AssertionError, assert_equals, Build(test_xml).name, "fail")