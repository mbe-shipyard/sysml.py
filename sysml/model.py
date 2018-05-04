"""
The `Model` class is used to instantiate a central namespace for a SysML model by subsuming stereotypes into mode elements or model relationships.

---------

Model elements and relationships are the building blocks that make up the 9 SysML diagrams
"""
from sysml.stereotypes import *
import re
import uuid

# developer notes: to use hidden vs unhidden attributes

class Model(object):
    """This class defines a SysML model for subsuming stereotypes into model elements or relationships.
    """

    # Dictionary of valid model elements. key: stereotype [string], value: stereotype [class]
    _validElements = {
        "block":Block,
        "requirement":Requirement,
        "constraint":Constraint,
        "package":Package
    }

    # Dictionary of valid model relationships. key: stereotype [string], value: valid stereotype nodes [list of classes]
    _validRelationships = {
        "containment":{
            "source":[Block],
            "target":[Block]},
        "inheritance":{
            "source":[Block],
            "target":[Block]},
        "association":{
            "source":[Block],
            "target":[Block]},
        "generalization":{
            "source":[Block],
            "target":[Block]},
        "partProperty":{
            "source":[Block],
            "target":[Block]},
        "valueProperty":{
            "source":[Block],
            "target":[Block]},
        "referenceProperty":{
            "source":[Block],
            "target":[Block]},
        "flowProperty":{
            "source":[Block],
            "target":[Block]}
    }

    def __init__(self, label=None, elements={}, relationships={}):
        # Model label
        self._label = label
        # All model elements stored as a dictionary of key-value pairs
        self._elements = elements
        # All model relationships stored as a dictionary of key-value pairs
        self._relationships = relationships

    def __setitem__(self, key, item):
        "Sets/overwrites stereotype-valid model element or relationship into model"
        if self._isValidElementKey(key):
            self._setElement(key, item)
        elif self._isValidRelationshipKey(key):
            self._setRelationship(key, item)
        else:
            raise ValueError(repr(key) + " is not a valid key. Keys should be a string containing a dash-separated stereotype and integer, e.g., 'partProperty-42' ")

    def __getitem__(self, key):
        "Returns data for key-specified model element or relationship"
        if key in self._elements.keys():
            return self._elements[key]
        elif key in self._relationships.keys():
            return self._relationships[key]
        else:
            raise ValueError(repr(key) + " is not a valid key. Keys should be a string containing a dash-separated stereotype and integer, e.g., 'partProperty-42' ")

    @property
    def elements(self):
        "Returns dictionary of model elements"
        return self._elements

    @property
    def relationships(self):
        "Returns dictionary of relationships"
        return self._relationships

    @elements.setter
    def elements(self, elements):
        """Sets/rewrites model elements for entire model by passing model elements as key-value pairs.

        Note: model elements must be valid stereotypes.
        """
        if type(elements) is not dict:
            raise TypeError(repr(elements) + " must be a dictionary.")
        else:
            for key in elements.keys():
                self._setElements(key,elements[key])

    @relationships.setter
    def relationships(self, relationships):
        """Sets relationships to user-defined dictionary.

        Note: model relationships must be valid stereotypes.
        """
        for key in relationships.keys():
            if not self._isValidElement(key):
                raise ValueError(key + " is not a valid key. Keys should be a string containing a dash-separated stereotype and integer, e.g., 'partProperty-42' ")
            if not self._isValidRelationship(relationships[key]["source"]):
                raise TypeError(relationships[key] + " is not a valid stereotype.")
        self._relationships = relationships

    def _setElement(self, key, element):
        # if not self._isValidElementKey(key):
        #     raise ValueError(key + " is not a valid key. Keys should be a string containing a dash-separated stereotype and integer, e.g., 'block-42' ")
        if not self._isValidElement(element):
            raise TypeError(repr(element) + " is not a valid stereotype.")
        else:
            self._elements[key] = element

            self._elements[key].uuid = str(uuid.uuid1())

    def _setRelationship(self, key, edge):
        # if not self._isValidRelationshipKey(key):
        #     raise ValueError(key + " is not a valid key. Keys should be a string containing a dash-separated stereotype and integer, e.g., 'block-42' ")
        stereotypeName, id_no = key.split('-')
        for target in edge['target']:
            if target not in self._validRelationships[stereotypeName]['target']:
                raise TypeError(repr(target) + " is not a valid target for " + stereotypeName)
        if edge['source'] not in self._validRelationships[stereotypeName]['source']:
            raise TypeError(repr(edge['source']) + " is not a valid source for " + stereotypeName)
        else:
            self._relationships[key] = edge
            if not hasattr(self._relationships[key], 'uuid'):
                self._relationships[key].uuid = str(uuid.uuid1())

    @classmethod
    def _isValidElementKey(cls, key):
        stereotypeName, id_no = key.split('-')
        return stereotypeName in cls._validElements.keys() and isinstance(int(id_no),int)

    @classmethod
    def _isValidElement(cls, item):
        return type(item) in cls._validElements.values()

    @classmethod
    def _isValidRelationshipKey(cls, key):
        stereotypeName, id_no = key.split('-')
        return stereotypeName in cls._validRelationships.keys() and isinstance(int(id_no),int)

    @classmethod
    def _isValidSource(cls, relationshipKey, source):
        return source in cls._validRelationships[relationshipKey]['source']

    @classmethod
    def _isValidTarget(cls, relationshipKey, target):
        return target in cls._validRelationships[relationshipKey]['target']
