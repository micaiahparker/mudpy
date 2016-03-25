from xml.etree.ElementTree import fromstring

from nose.tools import *

from game.build import Build, BuildException
from game.tools import get_buildable_classes
import game

test_xml = fromstring("<build name='Buildable' desc='A buildable object'/>")
b = Build(test_xml)


def test_build():
    """testing Build"""
    assert b


def test_build_name():
    """testing Build name"""
    assert b.name == 'Buildable'


def test_build_desc():
    assert b.desc == 'A buildable object'


def test_build_exception():
    assert_raises(BuildException, Build, fromstring("<build name='' desc=''><bad/></build>"))


def test_get_buildable():
    assert_equals(get_buildable_classes(game)['build'].__name__, Build.__name__)
