"""
The `stereotypes` module contains all model elements that are valid for use by the `model` class

---------

Model elements are the building blocks that make up the 9 SysML diagrams
"""

import uuid

# developer notes: to use hidden vs unhidden attributes

class Block(object):
    """This class defines a block

    Parameters
    ----------
    label : string, default None

    values : dict, default None

    parts : list, default None

    references : list, default None

    flowProperties : dict, default None


    Examples
    --------
    >>> warpcore = Block(label='warp core',
    ...                 parts=[antimatterinjector, Dilithiumcrystalchamber],
    ...                 flow={'in':{'inflow':'antimatter'}, 'out':{'outflow':'power'}})
    ...                 references=[antimatter])
    >>> warpdrive = Block(label='warp drive',
    ...                 values={'class-7'},
    ...                 parts=[antimattercontainment, warpcore, plasmainducer],

    """

    _stereotype = "block"
    _id_no = 0
    #tk: need to fix id_no state; store all existing id_no's in a list?

    def __init__(self, label=None, values=None, parts={}, references=None, flowProperties=None, stereotype=['block']):
        # Label
        if label is None:
            Block._id_no += 1
            self._label = 'Block' + str(Block._id_no)
        elif type(label) is not str:
            raise TypeError(label + " must be a string")
        else:
            self._label = label
        ## Part Property
        if type(parts) is not dict:
            raise TypeError(parts + " must be a dict")
        elif parts is dict:
            for part in parts:
                if not isinstance(part, Block): #tk: change to accept block or list of blocks
                    raise TypeError(part + " must be a Block")
        else:
            self._parts = parts
        """
        ## Value Property
        if type(values) is dict:
            self._values = values
        else:
            raise TypeError("argument is not a dictionary!")
        ## Reference Property
        if references is None:
            self._references = []
        elif type(references) is list: #tk: change to accept block or list of blocks
            self._references = references
        else:
            raise TypeError("argument is not a list!")
        ## Flow Property
        if flows is None:
            self._flowProperties = {}
        elif type(flowProperties) is dict:
            self._flowProperties = flowProperties
        else:
            raise TypeError("argument is not a dictionary!")
        ## Operations
        self.operations = []
        ## Constraints
        self.constaints = []
        """
    def __repr__(self):
        return "\xab" + self._stereotype + "\xbb '{}'".format(self._label)

    ## Getters
    @property
    def label(self):
        "Returns block label"
        return self._label

    @property
    def stereotype(cls):
        return cls._stereotype

    @property
    def uuid(self):
        "Returns block uuid"
        return self._uuid

    @property
    def parts(self):
        return self._parts

    @property
    def values(self):
        return self._values

    @property
    def references(self):
        return self._references

    @property
    def flows(self):
        return self._flowProperties

    ## Setters
    @label.setter
    def label(self, label):
        "Sets block label"
        if type(label) is not str:
            raise TypeError(label + " must be a string")
        else:
            self._label = label

    @uuid.setter
    def uuid(self, UUID):
        "Sets uuid"
        try:
            uuid.UUID(UUID, version=1)
            self._uuid = UUID
        except:
            raise ValueError(UUID + " must be a valid uuid of type, string")

    def add_part(self, label):
        """Creates a block element in block"""
        if type(label) is str:
            self._setElement(label, Block(label))
        else:
            raise TypeError(label + " must be a string")

    ## Structural Diagrams
    def bdd(self):
        """Generates a BlockDefinitionDiagram

        A block definition diagram describes the system hierarchy and system/component classifications.
        """
        pass

    def ibd(self):
        """Generates an internal block diagram

        The internal block diagram describes the internal structure of a system in terms of its parts, ports, and connectors.
        """
        pass

    ## Parametric Diagrams
    def par(self):
        """Generates a parametric diagram

        The parametric diagram represents constraints on system property values such as performance, reliability, and mass properties, and serves as a means to integrate the specification and design models with engineering analysis models.
        """
        pass

    def _generateKey(self, element, maxId_no):
        if self._isValidElement(element):
            for validElement in self._validElements.keys():
                if isinstance(element, self._validElements[validElement]):
                    for id_no in range(1, maxId_no+1):
                        newKey = validElement + "-" + str(id_no)
                        if newKey not in self._parts.keys():
                            return newKey
        elif self._isValidRelationship(element):
            for validRelationship in self._validRelationships.keys():
                if element["relationshipType"] is validRelationship:
                    for id_no in range(1, maxId_no+1):
                        newKey = validRelationship + "-" + str(id_no)
                        if newKey not in self._relationships.keys():
                            return newKey
        else:
            raise TypeError(element + " is not a valid element.")

    def _setElement(self, key, element):
        if key is None:
            key = self._generateKey(element)
        if not self._isValidElement(element):
            raise TypeError(repr(element) + " is not a valid model element.")
        else:
            self._parts[key] = element
            self._parts[key].uuid = str(uuid.uuid1())

    @classmethod
    def _isValidElement(cls, element):
        return isinstance(element, Block)

    # @parts.setter
    # def parts(self, *partv):
    #     """add one or more Blocks to parts
    #
    #     """
    #     for part in partv:
    #         if type(part) is Block:
    #             self._parts.append(part)
    #         else:
    #             raise TypeError("argument is not a 'Block'!")
    # @references.setter
    # def references(self, *referencev):
    #     """add one or more Blocks to references
    #
    #     """
    #     for reference in referencev:
    #         if type(reference) is Block:
    #             self._references.append(reference)
    #         else:
    #             raise TypeError("argument is not a 'Block'!")
    # @values.setter
    # def values(self, values):
    #     """add values dictionary to values
    #
    #     """
    #     if type(values) is dict:
    #         for key in values:
    #             if type(key) is str:
    #                 self.values[key] = values[key]
    #             else:
    #                 raise TypeError("key is not a string!")
    #     else:
    #         raise TypeError("argument is not a dictionary!")
    # @flowProperties.setter
    # def flowProperties(self, flowProperties):
    #     """add flowProperties dictionary to flowProperties
    #
    #     """
    #     if type(flowProperties) is dict:
    #         for flowPort in flowProperties:
    #             if type(flowPort) is str:
    #                 self._flowProperties[flowPort] = flowProperties[flowPort]
    #             else:
    #                 raise TypeError("key is not a string!")
    #     else:
    #         raise TypeError("argument is not a dictionary!")

class Requirement(object):
    """This class defines a requirement"""

    _stereotype = "requirement"
    _id_no = 0
    #tk: need to fix id_no state; store all existing id_no's in a list?

    def __init__(self, label=None, txt=None, id_no=None):
        # ID no.
        if id_no is None:
            Requirement._id_no += 1
            self._id_no = 'ID' + str(Requirement._id_no).zfill(3)
        elif type(id_no) in [int,float]:
            self._id_no = 'ID' + str(id_no).zfill(3)
        else:
            raise TypeError("argument is not int or float!")
        # Label
        if label is None:
            self._label = 'Requirement' + str(self._id_no)
        elif type(label) is str:
            self._label = label
        else:
            raise TypeError("argument is not a string!")
        # Text
        if txt is None:
            self.txt = ''
        elif type(label) is str:
            self.txt = txt
        else:
            raise TypeError("argument is not a string!")
        # # Satisfy
        # if satisfy is None:
        #     self._satisfy = []
        # elif type(satisfy) is []: #tk: change to accept block or list of blocks
        #     self._satisfy = satisfy
        # # Verify
        # if verify is None:
        #     self._verify = []
        # elif type(verify) is []: #tk: change to accept block or list of blocks
        #     self._verify = verify
        # # Refine
        # if refine is None:
        #     self.refine = []
        # elif type(refine) is []: #tk: change to accept block or list of blocks
        #     self._refine = refine
        # # Trace
        # if trace is None:
        #     self.trace = []
        # elif type(trace) is []: #tk: change to accept block or list of blocks
        #     self._trace = trace
    def __repr__(self):
        return "\xab" + self._stereotype + "\xbb '{}'".format(self._label)

    @property
    def stereotype(cls):
        return cls._stereotype

    @property
    def uuid(self):
        "Returns block uuid"
        return self._uuid

    ## Set requirement relations
    # def satisfiedBy(self, *sourcev):
    #     for source in sourcev:
    #         self._satisfy.append(source)
    # def refinedBy(self, *sourcev):
    #     for source in sourcev:
    #         self._refine.append(source)
    # def verifiedBy(self, *sourcev):
    #     for source in sourcev:
    #         self._verify.append(source)

    @uuid.setter
    def uuid(self, UUID):
        "Sets uuid"
        try:
            uuid.UUID(UUID, version=1)
            self._uuid = UUID
        except:
            raise ValueError(UUID + " must be a valid uuid of type, string")

    def req(self):
        """Generates a requirement diagram

        The requirements diagram captures requirements hierarchies and requirements derivation, and the satisfy and verify relationships allow a modeler to relate a requirement to a model element that satisfies or verifies the requirements.
        """
        pass

class ConstraintBlock(object):
    """This class defines a constraint"""

    def __init__(self):
        pass

    ## Structural Diagrams
    def bdd(self):
        """Generates a BlockDefinitionDiagram

        A block definition diagram describes the system hierarchy and system/component classifications.
        """
        pass

    ## Parametric Diagrams
    def par(self):
        """Generates a parametric diagram

        The parametric diagram represents constraints on system property values such as performance, reliability, and mass properties, and serves as a means to integrate the specification and design models with engineering analysis models.
        """
        pass

class Package(object):
    """This class defines a package"""

    _validElements = {
        "block":Block,
        "requirement":Requirement,
        "constraint":ConstraintBlock,
    }

    _stereotype = "package"

    def __init__(self, label=None, elements={}):
        self._label = label
        self._elements = elements

    def __setitem__(self, key, element):
        "Sets/overwrites element-valid model element or relationship into model"
        if self._isValidElement(element):
            self._setElement(key, element)
        # elif self._isValidRelationshipKey(key):
        #     self._setRelationship(key, element)
        else:
            raise ValueError(repr(key) + " is not a valid key. Keys should be a string containing a dash-separated element and integer, e.g., 'partProperty-42' ")

    def __getitem__(self, key):
        "Returns data for key-specified model element or relationship"
        if key in self._elements.keys():
            return self._elements[key]
        # elif key in self._relationships.keys():
        #     return self._relationships[key]
        else:
            raise ValueError(repr(key) + " is not a valid key. Keys should be a string containing a dash-separated element and integer, e.g., 'partProperty-42' ")

    def __repr__(self):
        return "\xab" + self._stereotype + "\xbb '{}'".format(self._label)

    @property
    def label(self):
        "Returns block label"
        return self._label

    @property
    def elements(self):
        return self._elements

    @property
    def stereotype(cls):
        return cls._stereotype

    @property
    def uuid(self):
        "Returns block uuid"
        return self._uuid

    @uuid.setter
    def uuid(self, UUID):
        "Sets uuid"
        try:
            uuid.UUID(UUID, version=1)
            self._uuid = UUID
        except:
            raise ValueError(UUID + " must be a valid uuid of type, string")

    def add_relation(self, source, target, relationType):
        """Creates a requirement element in package"""
        if self._isValidRelation({'source': source, 'target': target, 'relationType': relationType}):
            self._setRelation(source, target, relationType)
        else:
            raise TypeError(label + " must be a string")

    def add_block(self, label):
        """Creates a block element in package"""
        if type(label) is str:
            self._setElement(label, Block(label))
        else:
            raise TypeError(label + " must be a string")

    def add_requirement(self, label, txt):
        """Creates a requirement element in package"""
        if type(label) is str:
            self._setElement(label, Requirement(label, txt))
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

    ## Behavior
    def uc(self):
        """Generates a use case diagram

        A use-case diagram provides a high-level description of functionality that is achieved through interaction among systems or system parts.
        """
        pass

    ## Requirement Diagram
    def req(self):
        """Generates a requirement diagram

        The requirements diagram captures requirements hierarchies and requirements derivation, and the satisfy and verify relationships allow a modeler to relate a requirement to a model element that satisfies or verifies the requirements.
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

    def _isValidElement(self, element):
        return type(element) in self._validElements.values()

    def _setRelation(self, key, relation):
        self._elements[key] = relation

    def _isValidRelation(self, source, target, relationType):
        return type(source) in self._validRelations[relationType]['source'] and type(target) in self._validRelations[relationType]['target']

class StateMachine(object):
    """This class defines a state"""

    def __init__(self):
        pass

    def stm(self):
        """Generates a state machine diagram for a valid model element key

        The state machine diagram describes the state transitions and actions that a system or its parts perform in response to events.
         """
        pass

class Activity(object):
    """This class defines a activity"""

    def __init__(self):
        pass

    ## Behavioral Diagrams
    def act(self):
        """Generates an activity diagram for a valid model element key

        The activity diagram represents the flow of data and control between activities.
        """
        pass

class Interaction(object):
    """This class defines an interaction"""

    def __init__(self):
        pass

    ## Behavioral Diagrams
    def sd(self):
        """Generates a sequence diagram

        A sequence diagram represents the interaction between collaborating parts of a system.
        """
        pass
