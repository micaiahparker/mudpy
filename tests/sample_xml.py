from xml.etree.ElementTree import fromstring


def from_string(func, *args):
    def new_func():
        return fromstring(func(*args))
    return new_func


@from_string
def sample_build():
    return "<build name='Buildable' desc='A buildable object'/>"


@from_string
def sample_build_unknown():
    return "<build name='Buildable' desc='Contains a bad tag'><bad/></build>"


@from_string
def sample_build_gameobject():
    return "<game_object name='Test' desc='The First Game Object'></game_object>"

