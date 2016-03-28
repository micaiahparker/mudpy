from nose.tools import *
import game
from game.tools import get_buildable_classes
from game.build import *
from tests.sample_xml import *

test_xml = sample_build()
b = Build(test_xml)
Build.known = get_buildable_classes(__package__)


class TestBuildable(Build):
    tag = 'test'


def test_build():
    """testing Build"""
    assert b


def test_build_name():
    """testing Build name"""
    assert b.name == 'Buildable'


def test_build_desc():
    assert b.desc == 'A buildable object'


def test_build_unknown():
    assert_raises(BuildUnknownException, Build, sample_build_unknown())


def test_build_no_name():
    assert_raises(BuildNoNameException, Build, sample_build_no_name())


def test_get_buildable():
    assert_equals(get_buildable_classes(game)['build'].__name__, Build.__name__)
