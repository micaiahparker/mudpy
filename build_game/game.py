from build_game import build, rooms


class Game(build.Build):
    tag = 'game'
    build_from = [rooms.__name__]
    containers = {'rooms': 'room'}
