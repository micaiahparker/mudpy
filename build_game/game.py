from build_game import build, game_objects


class Game(build.Build):
    tag = 'game'
    build_from = [game_objects.__name__]
