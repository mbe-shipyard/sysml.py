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
    name : string, default None

    values : dict, default None

    parts : dict, default None

    references : list, default None

    flowProperties : dict, default None

    """

    _id_no = 0 #tk: need to fix id_no state; store all existing id_no's in a list?

    def __init__(self, name=None, values={}, parts={}, constraints={}, references=None, flowProperties=None, stereotypes=set(), multiplicity=1):
        """Note: Block() class is intended for internal use by Model() class"""

        """Stereotype"""
        if type(stereotypes) is not set:
            raise TypeError(str(stereotypes) + " must be a set")
        else:
            for i in stereotypes:
                if type(i) is not str:
                    raise TypeError(str(i) + " must be a string")
            self._stereotypes = set({Block.__name__.lower()}).union(stereotypes)

        """Label"""
        if name is None:
            Block._id_no += 1
            self._name = 'Block' + str(Block._id_no)
        elif type(name) is not str:
            raise TypeError(str(name) + " must be a string")
        else:
            self._name = name

        """Part Property"""
        if type(parts) is not dict:
            raise TypeError(str(parts) + " must be a dict")
        else:
            for key in parts:
                if type(key) is not str:
                    raise TypeError(str(key) + " must be a string")
                elif not isinstance(parts[key], Block): #tk: change to accept block or list of blocks
                    raise TypeError(str(part[key]) + " must be a Block")
            self._parts = parts

        """Value Property"""
        if type(values) is not dict:
            raise TypeError(str(values) + " must be a dict")
        else:
            for key in values:
                if type(key) is not str:
                    raise TypeError(str(key) + " must be a string")
                elif type(values[key]) is not int or type(values[key]) is not float or not hasattr(values[key],'units'):
                    raise TypeError(str(values[key]) + " must be an int, float, or have attribute 'unit'")
            self._values = values

        """Constraint Property"""
        if type(constraints) is not dict:
            raise TypeError(str(constraints) + " must be a dict")
        else:
            for key in constraints:
                if type(key) is not str:
                    raise TypeError(str(key) + " must be a string")
                if not isinstance(constraints[key], ConstraintBlock):
                    raise TypeError(str(constraints[key]) + " must be a ConstraintBlock")
            self._constraints = constraints

        """Multiplicity"""
        if type(multiplicity) is not int:
            raise TypeError(str(multiplicity) + " must be an int'")
        else:
            self._setMultiplicity(multiplicity)

        """UUID"""
        self._uuid = str(uuid.uuid1())

        """
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
        _stereotypes = ""
        for _stereotype in self._stereotypes:
            _stereotypes += "\xab" + _stereotype + "\xbb "
        return _stereotypes + "\n{}".format(self._name)

    ## Getters
    @property
    def name(self):
        "Returns block name"
        return self._name

    @property
    def stereotypes(self):
        return self._stereotypes

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

    @property
    def multiplicity(self):
        return self._multiplicity

    ## Setters
    @name.setter
    def name(self, name):
        "Sets block name"
        if type(name) is not str:
            raise TypeError(str(name) + " must be a string")
        else:
            self._name = name

    @multiplicity.setter
    def multiplicity(self, multiplicity):
        self._setMultiplicity(multiplicity)

    def add_part(self, name, multiplicity=1):
        """Creates a block element in block"""
        if type(name) is not str:
            raise TypeError(str(name) + " must be a string")
        else:
            self._addPart(name, Block(name), multiplicity)

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

    def _generateKey(self, elementType):
        if self._isValidElementType(elementType):
            for validElement in Package._validElementTypes:
                if elementType is validElement or elementType is Package:
                    for id_no in range(1, len(self._elements)+1):
                        newKey = validElement.__name__.lower() + str(id_no)
                        if newKey not in self._elements.keys():
                            return newKey
        else:
            raise TypeError(str(element) + " is not a valid model element.")

    def _addPart(self, key, element, multiplicity):
        if not self._isValidElement(element):
            raise TypeError(str(element) + " is not a valid model element")
        if key is None:
            key = self._generateKey(element)
        if type(multiplicity) is not int:
            raise TypeError(str(multiplicity) + " must be a positive int")
        elif not multiplicity > 0:
            raise ValueError(str(multiplicity) + " must be a positive int")
        else:
            self._parts[key] = element
            self._parts[key]._multiplicity = multiplicity

    def _setMultiplicity(self, multiplicity):
        if type(multiplicity) is not int:
            raise TypeError(str(multiplicity) + " must be a positive int")
        elif not multiplicity > 0:
            raise ValueError(str(multiplicity) + " must be a positive int")
        else:
            self._multiplicity = multiplicity

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

    _id_no = 0 #tk: need to fix id_no state; store all existing id_no's in a list?

    def __init__(self, name=None, txt=None, id_no=None):
        self._stereotypes = set({Requirement.__name__.lower()})

        """ID no."""
        if id_no is None:
            Requirement._id_no += 1
            self._id_no = 'ID' + str(Requirement._id_no).zfill(3)
        elif type(id_no) in [int, float]:
            self._id_no = 'ID' + str(id_no).zfill(3)
        else:
            raise TypeError(str(id_no) + " must be an int or float")

        """Label"""
        if name is None:
            self._name = 'Requirement' + str(self._id_no)
        elif type(name) is not str:
            raise TypeError(str(name) + " must be a string")
        else:
            self._name = name

        """Text"""
        if txt is None:
            self.txt = ''
        elif type(name) is str:
            self.txt = txt
        else:
            raise TypeError(str(name) + " must be a string")

        """UUID"""
        self._uuid = str(uuid.uuid1())

    def __repr__(self):
        _stereotypes = ""
        for _stereotype in self._stereotypes:
            _stereotypes += "\xab" + _stereotype + "\xbb "
        return _stereotypes + "\n{}".format(self._name)

    @property
    def stereotypes(self):
        return self._stereotypes

    @property
    def uuid(self):
        "Returns block uuid"
        return self._uuid

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

class Dependency(object):
    """This class defines a dependency"""

    # _validStereotypes = set({'deriveReqt','refine','satisfy','verify'})

    def __init__(self, supplier, client, stereotype):
        if stereotype is 'deriveReqt':
            if type(supplier) is not Requirement:
                raise TypeError(str(supplier) + ' is not a Requirement')
            elif type(client) is not Requirement:
                raise TypeError(str(client) + ' is not a Requirement')
            else:
                self._supplier = supplier
                self._client = client
                self._stereotype = stereotype
        elif stereotype is 'satisfy':
            if type(supplier) is not Requirement:
                raise TypeError(str(supplier) + ' is not a Requirement')
            elif type(client) is not Block:
                raise TypeError(str(client) + ' is not a Block')
            else:
                self._supplier = supplier
                self._client = client
                self._stereotype = stereotype
        else:
            raise ValueError(str(stereotype) + ' is not a valid dependency stereotype')

        """UUID"""
        self._uuid = str(uuid.uuid1())

    @property
    def supplier(self):
        return self._supplier

    @property
    def client(self):
        return self._client

    @property
    def stereotype(self):
        return self._stereotype

    @property
    def uuid(self):
        "Returns block uuid"
        return self._uuid

class Package(object):
    """This class defines a package"""

    _id_no = 0
    _validElementTypes = set({Block, Requirement, ConstraintBlock, Dependency})

    def __init__(self, name=None, elements={}):

        """Stereotype"""
        self._stereotypes = set({"package"})

        """Label"""
        if name is None:
            Package._id_no += 1
            self._name = 'Package' + str(Package._id_no)
        elif type(name) is not str:
            raise TypeError(str(name) + " must be a string")
        else:
            self._name = name

        """Elements"""
        self._elements = elements

        """UUID"""
        self._uuid = str(uuid.uuid1())

    def __getitem__(self, key):
        "Returns data for key-specified model element or relationship"
        return self._elements[key]

    def __repr__(self):
        _stereotypes = ""
        for _stereotype in self._stereotypes:
            _stereotypes += "\xab" + _stereotype + "\xbb "
        return _stereotypes + "\n{}".format(self._name)

    @property
    def name(self):
        "Returns block name"
        return self._name

    @property
    def elements(self):
        return self._elements

    @property
    def stereotypes(self):
        return self._stereotypes

    @property
    def uuid(self):
        "Returns block uuid"
        return self._uuid

    def add_package(self, name):
        """Creates a package element in model"""
        self._setElement(name, Package(name))

    def add_block(self, name):
        """Creates a block element in package"""
        if type(name) is str:
            self._setElement(name, Block(name))
        else:
            raise TypeError(str(name) + " must be a string")

    def add_requirement(self, name, txt):
        """Creates a requirement element in package"""
        if type(name) is str:
            self._setElement(name, Requirement(name, txt))
        else:
            raise TypeError(str(name) + " must be a string")

    def add_dependency(self, supplier, client, stereotype):
        """Creates a dependency element in package"""
        # element = Dependency(supplier, client, stereotype)
        key = self._generateKey(Dependency)
        self._setElement(key, Dependency(supplier, client, stereotype))

    def remove_element(self, key):
        """Removes a model element from package"""
        pass

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

    def _generateKey(self, elementType):
        if self._isValidElementType(elementType):
            for validElement in Package._validElementTypes:
                if elementType is validElement or elementType is Package:
                    for id_no in range(1, len(self._elements)+1):
                        newKey = validElement.__name__.lower() + str(id_no)
                        if newKey not in self._elements.keys():
                            return newKey
        else:
            raise TypeError(str(element) + " is not a valid model element.")

    def _setElement(self, key, element):
        # if key is None:
        #     key = self._generateKey(element)
        if not self._isValidElementType(type(element)):
            raise TypeError(str(element) + " is not a valid model element.")
        else:
            self._elements[key] = element

    def _isValidElementType(self, elementType):
        return elementType in self._validElementTypes or elementType is Package

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

    _id_no = 0
    # _validElementTypes = set({Lifeline, Message, Occurence})

    def __init__(self, name=None, elements={}):

        """Stereotype"""
        self._stereotypes = set({"interaction"})

        """Label"""
        if name is None:
            Interaction._id_no += 1
            self._name = 'Package' + str(Interaction._id_no)
        elif type(name) is not str:
            raise TypeError(str(name) + " must be a string")
        else:
            self._name = name

        """Elements"""
        self._elements = elements

        """UUID"""
        self._uuid = str(uuid.uuid1())

    def __repr__(self):
        _stereotypes = ""
        for _stereotype in self._stereotypes:
            _stereotypes += "\xab" + _stereotype + "\xbb "
        return _stereotypes + "\n{}".format(self._name)

    @property
    def name(self):
        "Returns block name"
        return self._name

    @property
    def elements(self):
        return self._elements

    @property
    def stereotypes(self):
        return self._stereotypes

    @property
    def uuid(self):
        "Returns block uuid"
        return self._uuid
    def add_lifeline(self):
        pass

    ## Behavioral Diagrams
    def sd(self):
        """Generates a sequence diagram

        A sequence diagram represents the interaction between collaborating parts of a system.
        """
        pass
