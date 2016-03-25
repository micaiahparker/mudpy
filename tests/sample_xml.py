from xml.etree.ElementTree import fromstring


def from_string_dec(func, *args):
    def new_func():
        return fromstring(func(*args))
    return new_func


@from_string_dec
def sample_build():
    return "<build name='Buildable' desc='A buildable object'/>"


@from_string_dec
def sample_build_bad():
    return "<build name='' desc=''><bad/></build>"


@from_string_dec
def sample_object():
    return "<object name='test' desc='Testing This Works'/>"


