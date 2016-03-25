from xml.etree.ElementTree import fromstring


def from_string_dec(func, *args):
    def new_func():
        return fromstring(func(*args))
    return new_func


@from_string_dec
def basic_build_xml():
    return "<build name='Buildable' desc='A buildable object'/>"


