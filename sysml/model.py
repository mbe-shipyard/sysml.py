"""
The `Model` class is used to instantiate a central namespace for a SysML model by subsuming stereotypes into mode elements or model relationships.

---------

Model elements and relationships are the building blocks that make up the 9 SysML diagrams
"""
from sysml.stereotypes import *

# developer notes: to use hidden vs unhidden attributes

class Model(object):
    """This class defines a SysML model for subsuming stereotypes into model elements or relationships.
    """

    _validStereotypes = {"block":Block, "requirement":Requirement, "constraint":Constraint, "package":Package}

    def __init__(self, label=None, elements=None, relationships=None):
        # Model label
        self._label = label
        # List of model elements
        self._elements = elements
        # Relationship between model elements
        self._relationships = relationships
        # All model elements and model relationships are stored as key-value pairs, where keys are generated upon assimilation
        self._collective = {}

    def __setitem__(self, idKey, item):
        "Adds or rewrites stereotype-valid model element or relationship into model"
        try:
            stereotype, id_no = idKey.split('-')
            if stereotype in Model._validStereotypes.keys() and isinstance(int(id_no),int):
                stereotypeInstance = Model._validStereotypes[stereotype](label=item.label)
                self._collective[idKey] = stereotypeInstance
        except:
            raise TypeError(idKey + " is not a valid key. Keys should be a string containing a dash-separated stereotype and integer, e.g., 'block-42' ")

    def __getitem__(self, idKey):
        "Returns data for key-specified model element or relationship"
        return self._collective[idKey]

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
            if type(element) not in Model._validStereotypes.values():
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
