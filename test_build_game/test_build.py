from build_game.build import Build
from build_game import build
from xml.etree.ElementTree import fromstring
from nose.tools import *
test_xml = fromstring('<build name="test"/>')


def test_build_init():
    """test build init"""
    assert_true(Build(test_xml))


def test_build_tag():
    """test build tag"""
    assert_equals(Build.tag, 'build')


def test_build_build_from():
    """test build from"""
    assert_equals(Build.build_from, [build.__name__])


def test_build_name():
    """test build name"""
    assert_equals(Build(test_xml).name, "test")


def test_should_fail():
    """should fail"""
    assert_raises(AssertionError, assert_equals, Build(test_xml).name, "fail")


def test_build_before_update():
    """test build update"""
    assert_false('test' in Build(test_xml).known)


def test_build_after_update():
    b = Build(test_xml)
    b.update()
    assert_true('test' in b.known.keys())
