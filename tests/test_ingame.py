from nose.tools import *
from game.ingame.game_objects import Object
from tests import sample_xml


def test_object_init():
    assert Object(sample_xml.sample_object())


