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

    def __init__(self, label=None, elements={}, relations={}):

        """Stereotype"""
        self._stereotypes = set({"model"})

        """Label"""
        if label is None:
            Model._id_no += 1
            self._label = 'Model' + str(Model._id_no)
        elif type(label) is not str:
            raise TypeError(label + " must be a string")
        else:
            self._label = label

        """Elements"""
        self._elements = elements

    def isValid(self):
        """Checks whether all requirements contained within model are satisfied by a «block» and verified by a «testCase»"""
        pass
