from build_game.build import Build

test_xml = ""


def test_build_init():
    assert Build(test_xml)


def test_build_tag():
    assert Build(test_xml).tag == 'build'
