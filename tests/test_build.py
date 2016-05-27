from game_build.build import *


def test_build():
    builder = MudpyGameBuilder('../game_files')
    assert builder.root
