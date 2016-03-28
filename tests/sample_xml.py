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
def sample_build_no_name():
    return "<build name='Buildable' desc='raises no name exception'><test/></build>"


@from_string
def sample_object():
    return "<object name='test' desc='Testing This Works'/>"
