from build_game import build


class Room(build.Build):
    tag = 'room'
    build_from = [__name__]