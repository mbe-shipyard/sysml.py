"""
The `Model` class is used to instantiate a central namespace for a SysML model by subsuming elements into mode elements or model relations.

---------

Model elements and relations are the building blocks that make up the 9 SysML diagrams
"""
from sysml.element import *
import uuid

# developer notes: to use hidden vs unhidden attributes

class Model(Package):
    """This class defines a SysML model for subsuming elements into model elements or relations.
    """

    _id_no = 0

    def __init__(self, name=None, elements={}):

        """Stereotype"""
        self._stereotypes = set({"model"})

        """Label"""
        if name is None:
            Model._id_no += 1
            self._name = 'Model' + str(Model._id_no)
        elif type(name) is not str:
            raise TypeError(str(name) + " must be a string")
        else:
            self._name = name

        """Elements"""
        self._elements = elements

    def isValid(self):
        """Checks whether all requirements contained within model are satisfied by a «block» and verified by a «testCase»"""
        pass
