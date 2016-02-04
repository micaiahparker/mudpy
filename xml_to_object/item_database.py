known = {}


def add_known(cls):
    known[cls.tag] = cls


def make_item(item):
    if item.tag in known:
        return known[item.tag](known)
    return None
