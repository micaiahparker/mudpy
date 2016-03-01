from xml.etree.ElementTree import fromstring
from system.game.build import Build

test_xml = fromstring("<build name='Buildable' desc='A buildable object'/>")
b = Build(test_xml)


def test_build():
    assert b


def test_build_name():
    assert b.name == 'Buildable'


def test_build_desc():
    assert b.desc == 'A buildable object'


def test_id_score():
    assert b.id_score(['Buildable']) == 2



