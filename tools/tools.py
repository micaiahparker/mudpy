from pkgutil import walk_packages
from inspect import isclass, getmembers


def get_modules(pkg):
    if type(pkg) == str:
        path = pkg
    else:
        path = pkg.__path__
    return [(finder, name) for finder, name, ispkg in walk_packages(path) if not ispkg]


def get_buildable_classes(pkg):
    ret = dict()
    for finder, name in get_modules(pkg):
        for cls_name, cls in getmembers(finder.find_loader(name)[0].load_module(name), isclass):
            if 'tag' in vars(cls).keys():
                ret[cls.tag] = cls
    return ret