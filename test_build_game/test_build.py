from build_game import build
from xml.etree.ElementTree import fromstring
from nose.tools import *

xml_string = """
    <build name="test">
        <test name="test_name" test_var = "1"/>
    </build>
"""

test_xml = fromstring(xml_string)


def test_build_init():
    """test build init"""
    assert_true(build.Build(test_xml))


def test_build_tag():
    """test build tag"""
    assert_equals(build.Build.tag, 'build')


def test_build_build_from():
    """test build from"""
    assert_equals(build.Build.build_from, [build.__name__])


def test_build_name():
    """test build name"""
    assert_equals(build.Build(test_xml).name, "test")


def test_should_fail():
    """should fail"""
    assert_raises(AssertionError, assert_equals, build.Build(test_xml).name, "fail")


def test_build_after_update():
    """test build after update"""
    b = build.Build(test_xml)
    assert_true('test' in b.known.keys())
