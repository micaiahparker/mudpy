from build_game import game, game_objects
from xml.etree.ElementTree import fromstring
from nose.tools import *

xml_string = """
    <game name="test">
        <room name="test room">
            <player name="test player"/>
        </room>
    </game>
"""

test_xml = fromstring(xml_string)


def test_game_init():
    """test build init"""
    assert_true(game.Game(test_xml))


def test_game_tag():
    """test build tag"""
    assert_equals(game.Game.tag, 'game')


def test_game_build_from():
    """test build from"""
    assert_equals(game.Game.build_from, [game.__name__, game_objects.__name__])


def test_game_name():
    """test build name"""
    assert_equals(game.Game(test_xml).name, "test")


def test_should_fail():
    """should fail"""
    assert_raises(AssertionError, assert_equals, game.Game(test_xml).name, "fail")


def test_build_after_update():
    """test build after update"""
    g = game.Game(test_xml)
    assert_true('room' in g.known.keys())


def test_child():
    """test child"""
    assert_true(game.Game(test_xml).rooms['test room'].players['test player'])