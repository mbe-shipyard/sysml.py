"""
The `Model` class is used to instantiate a central namespace for a SysML model by subsuming elements into mode elements or model relations.

---------

Model elements and relations are the building blocks that make up the 9 SysML diagrams
"""
from sysml.element import *
import uuid

# developer notes: to use hidden vs unhidden attributes

class Model(Package):
    """This class defines a SysML system model. A system model serves as the root namespace for subsuming all model elements (and relationships between elements) of a system.
    """

    def isValid(self):
        """Checks whether all requirements contained within model are satisfied by a «block» and verified by a «testCase»"""
        pass
