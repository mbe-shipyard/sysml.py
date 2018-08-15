"""
The `model.py` module is used to instantiate a central namespace for a SysML
model by subsuming elements into mode elements or model relations.
"""
from sysml.element import *

# developer notes: to use hidden vs unhidden attributes


class Model(Package):
    """This class defines a SysML system model. A system model serves as the
    root namespace for subsuming all model elements (and relationships between
    elements) of a system.
    """

    def isValid(self):
        """Checks whether all requirements contained within model are satisfied
        by a «block» and verified by a «testCase»"""
        pass
