"""
The `Model` class is used to instantiate a central namespace for a SysML model by subsuming stereotypes into mode elements or model relationships.

---------

Model elements and relationships are the building blocks that make up the 9 SysML diagrams
"""
from sysml.stereotypes import *
import re

# developer notes: to use hidden vs unhidden attributes

class Model(object):
    """This class defines a SysML model for subsuming stereotypes into model elements or relationships.
    """

    _validElements = {"block":Block, "requirement":Requirement, "constraint":Constraint, "package":Package}
    _validRelationships = {}

    def __init__(self, label=None, elements={}, relationships={}):
        # Model label
        self._label = label
        # All model elements stored as a dictionary of key-value pairs
        self._elements = elements
        # All model relationships stored as a dictionary of key-value pairs
        self._relationships = relationships

    def __setitem__(self, key, item):
        "Sets/overwrites stereotype-valid model element or relationship into model"
        if not self._isValidKey(key):
            raise ValueError(key + " is not a valid key. Keys should be a string containing a dash-separated stereotype and integer, e.g., 'block-42' ")
        if not self._isValidStereotype(item):
            raise TypeError(item + " is not a valid stereotype.")
        else:
            self._elements[key] = item

    def __getitem__(self, key):
        "Returns data for key-specified model element or relationship"
        if key in self._elements.keys():
            return self._elements[key]
        elif key in self._relationships.keys():
            return self._relationships[key]
        else:
            raise ValueError(key + " is not a valid key. Keys should be a string containing a dash-separated stereotype and integer, e.g., 'block-42' ")

    @property
    def elements(self):
        "Returns list of model elements"
        return self._elements

    @elements.setter
    def elements(self, elements):
        """Sets/rewrites model elements for entire model by passing model elements as key-value pairs.

        Note: model elements must be valid stereotypes.
        """
        if not type(elements) is dict:
            raise TypeError(elements + " must be a dictionary.")
        else:
            for key in elements.keys():
                if not self._isValidKey(key):
                    raise ValueError(key + " is not a valid key. Keys should be a string containing a dash-separated stereotype and integer, e.g., 'block-42' ")
                if not self._isValidStereotype(elements[key]):
                    raise TypeError(elements[key] + " is not a valid stereotype.")
            self._elements = elements

    @property
    def relationships(self):
        "Returns dictionary of relationships"
        return self._relationships

    # @relationships.setter
    # def relationships(self, relationships):
    #     """Sets relationships to user-defined dictionary.
    #
    #     Note: model relationships must be valid stereotypes.
    #     """
    #     for key in relationships:
    #         stereotype, id_no = key.split('-')
    #         if stereotype not in Model._validElements:
    #             raise TypeError(stereotype + "is not a valid stereotype.")
    #     self._relationships[key] = relationships[key]

    @classmethod
    def _isValidKey(cls, key):
        stereotypeName, id_no = key.split('-')
        return stereotypeName in cls._validElements.keys() or stereotypeName in cls._validRelationships.keys() and isinstance(int(id_no),int)

    @classmethod
    def _isValidStereotype(cls, item):
        return type(item) in cls._validElements.values() or type(item) in cls._validRelationships.values()
