from build_game import build


class Room(build.Build):
    tag = 'room'
    containers = {'players': 'player'}
    build_from = [__name__]


class Player(build.Build):
    tag = 'player'
