"""
The `Model` class is used to instantiate a central namespace for a SysML model by subsuming elements into mode elements or model relations.

---------

Model elements and relations are the building blocks that make up the 9 SysML diagrams
"""
from sysml.element import *
import uuid

# developer notes: to use hidden vs unhidden attributes

class Model(object):
    """This class defines a SysML model for subsuming elements into model elements or relations.
    """

    # Dictionary of valid model elements. key: element [string], value: element [class]
    _validElements = {
        "block":Block,
        "requirement":Requirement,
        "constraint":ConstraintBlock,
        "package":Package
    }

    # Dictionary of valid model relations. key: element [string], value: valid element nodes [list of classes]
    _validRelations = {
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

    def __init__(self, label=None, elements={}, relations={}):
        # Model label
        self._label = label
        # All model elements stored as a dictionary of key-value pairs
        self._elements = elements

    def __setitem__(self, key, element):
        "Sets/overwrites element-valid model element or relation into model"
        if self._isValidElementKey(key):
            self._setElement(key, element)
        elif self._isValidRelationKey(key):
            self._setRelation(key, element)
        else:
            raise ValueError(repr(key) + " is not a valid key. Keys should be a string containing a dash-separated element and integer, e.g., 'partProperty-42' ")

    def __getitem__(self, key):
        "Returns data for key-specified model element or relation"
        if key in self._elements.keys():
            return self._elements[key]
        elif key in self._relations.keys():
            return self._relations[key]
        else:
            raise ValueError(repr(key) + " is not a valid key. Keys should be a string containing a dash-separated element and integer, e.g., 'partProperty-42' ")

    @property
    def elements(self):
        "Returns dictionary of model elements"
        return self._elements

    @property
    def relations(self):
        "Returns dictionary of relations"
        return self._relations

    @elements.setter
    def elements(self, elements):
        """Sets/rewrites model elements for entire model by passing model elements as key-value pairs.

        Note: model elements must be valid elements.
        """
        if type(elements) is not dict:
            raise TypeError(repr(elements) + " must be a dictionary.")
        else:
            for key in elements.keys():
                self._setElements(key, elements[key])

    @relations.setter
    def relations(self, relations):
        """Sets relations to user-defined dictionary.

        Note: model relations must be valid elements.
        """
        if type(relations) is not dict:
            raise TypeError(repr(relations) + " must be a dictionary.")
        for key in relations.keys():
            elementName, id_no = key.split('-')
            if not self._isValidRelationKey(key):
                raise ValueError(key + " is not a valid key. Keys should be a string containing a dash-separated element and integer, e.g., 'partProperty-42' ")
            else:
                self._setRelation(key, relations[key])

    def add_elements(self, *elementv):
        "Sets/overwrites element-valid model element or relation into model"
        for element in elementv:
            key = self._generateKey(element, len(self._elements)+1)
            self._setElement(key, element)

    # def add_relations(self, *relationv):
    #     "Sets/overwrites element-valid model element or relation into model"
    #     for relation in relationv:
    #         key = self._generateKey(relation, len(self._relations)+1)
    #         self._setRelation(key, relation)

    def add_package(self, label=None):
        """Creates a package element in model"""
        if type(label) is str:
            self._setElement(label, Package(label))
        else:
            raise TypeError(label + " must be a string")

    ## Structural Diagrams
    def bdd(self):
        """Generates a BlockDefinitionDiagram

        A block definition diagram describes the system hierarchy and system/component classifications.
        """
        pass

    def pkg(self):
        """Generates a package diagram

        The package diagram is used to organize the model.
        """
        pass

    ## Behavioral Diagrams
    def uc(self):
        """Generates a use case diagram

        A use-case diagram provides a high-level description of functionality that is achieved through interaction among systems or system parts.
        """
        pass

    ## Requirement Diagrams
    def req(self):
        """Generates a requirement diagram

        The requirements diagram captures requirements hierarchies and requirements derivation, and the satisfy and verify relations allow a modeler to relate a requirement to a model element that satisfies or verifies the requirements.
        """
        pass

    def _generateKey(self, element, maxId_no):
        if self._isValidElement(element):
            for validElement in self._validElements.keys():
                if isinstance(element, self._validElements[validElement]):
                    for id_no in range(1, maxId_no+1):
                        newKey = validElement + "-" + str(id_no)
                        if newKey not in self._elements.keys():
                            return newKey
        elif self._isValidRelation(element):
            for validRelation in self._validRelations.keys():
                if element["relationType"] is validRelation:
                    for id_no in range(1, maxId_no+1):
                        newKey = validRelation + "-" + str(id_no)
                        if newKey not in self._relations.keys():
                            return newKey
        else:
            raise TypeError(element + " is not a valid element.")

    def _setElement(self, key, element):
        if key is None:
            key = self._generateKey(element)
        if not self._isValidElement(element):
            raise TypeError(repr(element) + " is not a valid model element.")
        else:
            self._elements[key] = element
            self._elements[key].uuid = str(uuid.uuid1())

    def _setRelation(self, key, relation):
        if relation["source"] not in self._elements.keys():
            raise TypeError(relations[key]["source"] + " does not exist in model.")
        if relation["target"] not in self._elements.keys():
            raise TypeError(relation["target"] + " does not exist in model.")
        if not self._isValidRelation(relation):
            raise TypeError(relation["source"] + " and " + relations["target"] + " are not a valid source-target pair for " + elementName)
        else:
            self._relations[key] = relation
            # if not hasattr(self._relations[key], 'uuid'):
            #     self._relations[key].uuid = str(uuid.uuid1())

    def _isValidRelation(self, relation):
        source = self._elements[relation["source"]]
        target = self._elements[relation["target"]]
        relationType = relation["relationType"]
        return type(source) in self._validRelations[relationType]['source'] and type(target) in self._validRelations[relationType]['target']

    @classmethod
    def _isValidElementKey(cls, key):
        elementName, id_no = key.split('-')
        return elementName in cls._validElements.keys() and isinstance(int(id_no),int)

    @classmethod
    def _isValidElement(cls, element):
        return type(element) in cls._validElements.values()

    @classmethod
    def _isValidRelationKey(cls, key):
        relation, id_no = key.split('-')
        return relation in cls._validRelations.keys() and isinstance(int(id_no),int)

    # @classmethod
    # def _isValidSource(cls, relation, source):
    #     return source in cls._validRelations[relation]['source']
    #
    # @classmethod
    # def _isValidTarget(cls, relation, target):
    #     return target in cls._validRelations[relation]['target']
