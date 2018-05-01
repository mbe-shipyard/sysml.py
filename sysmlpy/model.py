"""
The `Model` class consists of stereotypes which classify as either elements or relationships

---------

Model elements and relationships are the building blocks that make up the 9 SysML diagrams
"""
from sysmlpy.stereotypes import *
import traceback

# developer notes: to use hidden vs unhidden attributes

class Model(object):
    """This class defines a SysML model for subsuming stereotypes which classify as either model elements or relationships.
    """

    _validStereotypes = [Block, Requirement, Constraint, Package]
    #_validStereotypes = []

    def __init__(self, label=None, elements={}, relationships={}):
        self.label = label
        self._elements = elements
        self._relationships = relationships

    @property
    def elements(self):
        "Returns list of model elements"
        return self._elements

    @elements.setter
    def elements(self, elements):
        """Sets list of model elements.

        Note: model elements must be valid stereotypes.
        """
        for element in elements:
            if type(element) not in Model._validStereotypes:
                raise TypeError(element + "is not a valid stereotype.")
        self._elements = elements

    @property
    def relationships(self):
        "Returns dictionary of relationships"
        return self._relationships

    @relationships.setter
    def relationships(self, relationships):
        """Sets relationships to user-defined dictionary.

        Note: model relationships must be valid stereotypes.
        """
        for key in relationships:
            stereotype, id_no = key.split('-')
            if stereotype not in Model._validStereotypes:
                raise TypeError(stereotype + "is not a valid stereotype.")
        self._relationships[key] = relationships[key]
