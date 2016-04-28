from game.ingame.GameObject import GameObject
from tests.sample_xml import sample_build_gameobject


def test_gameobject():
    assert GameObject


def test_init():
    assert GameObject(sample_build_gameobject())


