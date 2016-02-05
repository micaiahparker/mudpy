from build_game import build, game_objects


class Game(build.Build):
    tag = 'game'
    build_from = [__name__, game_objects.__name__]
    containers = {'rooms': 'room'}

if __name__ == "__main__":
    from xml.etree.ElementTree import fromstring

    xml_string = """
    <game name="test">
        <room name="test room"/>
    </game>
    """

    Game(fromstring(xml_string))




