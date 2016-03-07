from xml.etree.ElementTree import fromstring
from system.game_objects.build import Build, BuildException
from nose.tools import *

test_xml = fromstring("<build name='Buildable' desc='A buildable object'/>")
b = Build(test_xml)


def test_build():
    assert b


def test_build_name():
    assert b.name == 'Buildable'


def test_build_desc():
    assert b.desc == 'A buildable object'


def test_id_no_tags():
    assert b.id_score() == 0


def test_id_score():
    assert b.id_score('Buildable') == 2


def test_build_exception():
    assert_raises(BuildException, Build, fromstring("<build name='' desc=''><bad/></build>"))



