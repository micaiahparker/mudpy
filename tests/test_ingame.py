from nose.tools import *
from game.ingame.game_objects import MudpyObject
from tests import sample_xml


def test_object_init():
    assert MudpyObject(sample_xml.sample_object())


