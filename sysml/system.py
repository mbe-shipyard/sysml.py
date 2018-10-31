"""
The `model.py` module is used to instantiate a central namespace for a SysML
model by subsuming elements into mode elements or model relations.
"""
from sysml.element import *
from yaml import dump as _dump
from yaml import load as _load

# developer notes: to use hidden vs unhidden attributes


class Model(Package):
    """This class defines a SysML system model. A system model serves as the
    root namespace for subsuming all model elements (and relationships between
    elements) of a system.
    """

    def to_yaml(self, filename):
        """ Write this Project to a yaml file """
        if type(filename) is str:
            with open(filename, 'w') as f:
                f.write(_dump(self))
        else:
            raise TypeError

    def isValid(self):
        """Checks whether all requirements contained within model are satisfied
        by a «block» and verified by a «testCase»"""
        pass


def read_yaml(filename=""):
    """ Load a project from a yaml file """
    with open(filename, 'r') as f:
        rv = _load(f.read())
        if type(rv) is Model:
            return rv
        else:
            raise TypeError(type(rv))
