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
    modelName : string, default None

    values : dict, default None

    parts : dict, default None

    references : list, default None

    flowProperties : dict, default None

    """

    _id_no = 0 #tk: need to fix id_no state; store all existing id_no's in a list?

    def __init__(self, modelName=None, typeName=None, parts={}, references=None, values={}, constraints={}, flowProperties=None, stereotypes=set(), multiplicity=1):
        """Note: Block() class is intended for internal use by Model() class"""

        "Check if constructor arguments are valid"
        if self._isValidBlockArgs(modelName, typeName, parts, references, values, constraints, flowProperties, stereotypes, multiplicity):
            pass

        """Stereotype"""
        self._stereotypes = set({'block'}).union(stereotypes)

        """Name"""
        if modelName is None:
            Block._id_no += 1
            self._modelName = 'block' + str(Block._id_no)
        else:
            self._modelName = modelName

        """Part Property"""
        self._parts = parts

        """Value Property"""
        self._values = values

        """Constraint Property"""
        self._constraints = constraints

        """Multiplicity"""
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
        return _stereotypes + "\n{}".format(self._modelName)

    ## Getters
    @property
    def modelName(self):
        "Returns block modelName"
        return self._modelName

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
    @modelName.setter
    def modelName(self, modelName):
        "Sets block modelName"
        if type(modelName) is not str:
            raise TypeError("'{}' must be a string".format(str(modelName)))
        else:
            self._modelName = modelName

    @multiplicity.setter
    def multiplicity(self, multiplicity):
        self._setMultiplicity(multiplicity)

    def new_part(self, modelName=None, typeName=None, parts={}, references=None, values={}, constraints={}, flowProperties=None, stereotypes=set(), multiplicity=1):
        """Creates a block element in block"""
        if type(multiplicity) is not int:
            raise TypeError("'{}' must be a positive int".format(str(multiplicity)))
        elif not multiplicity > 0:
            raise ValueError("'{}' must be a positive int".format(str(multiplicity)))
        if type(modelName) is not str:
            raise TypeError("'{}' must be a string".format(str(modelName)))
        elif modelName is None:
            Block._id_no += 1
            modelName =  'Block' + str(Block._id_no)
        key = _generateKey(modelName)
        self._parts[key] = Block(modelName, typeName, parts, references, values, constraints, flowProperties, stereotypes, multiplicity)

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

    def _setMultiplicity(self, multiplicity):
        if type(multiplicity) is not int:
            raise TypeError("'{}' must be a positive int".format(str(multiplicity)))
        elif not multiplicity > 0:
            raise ValueError("'{}' must be a positive int".format(str(multiplicity)))
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

    @staticmethod
    def _isValidBlockArgs(modelName, typeName, parts, references, values, constraints, flowProperties, stereotypes, multiplicity):
        """Stereotype"""
        if type(stereotypes) is not set:
            raise TypeError("'{}' must be a string".format(str(stereotypes)))
        else:
            for i in stereotypes:
                if type(i) is not str:
                    raise TypeError("'{}' must be a string".format(str(i)))

        """Name"""
        if modelName is not None and type(modelName) is not str:
            raise TypeError("'{}' must be a string".format(str(modelName)))

        """Part Property"""
        if type(parts) is not dict:
            raise TypeError(str(parts) + " must be a dict")
        else:
            for key in parts:
                if type(key) is not str:
                    raise TypeError("'{}' must be a string".format(str(key)))
                elif not isinstance(parts[key], Block): #tk: change to accept block or list of blocks
                    raise TypeError(str(part[key]) + " must be a Block")

        """Value Property"""
        if type(values) is not dict:
            raise TypeError(str(values) + " must be a dict")
        else:
            for key in values:
                if type(key) is not str:
                    raise TypeError("'{}' must be a string".format(str(key)))
                elif type(values[key]) is not int or type(values[key]) is not float or not hasattr(values[key],'units'):
                    raise TypeError("'{}' must be an int, float, or have attribute 'unit'".format(str(values[key])))

        """Constraint Property"""
        if type(constraints) is not dict:
            raise TypeError(str(constraints) + " must be a dict")
        else:
            for key in constraints:
                if type(key) is not str:
                    raise TypeError("'{}' must be a string".format(str(key)))
                if not isinstance(constraints[key], ConstraintBlock):
                    raise TypeError("'{}' must be a ConstraintBlock".format(str(constraints[key])))

        """Multiplicity"""
        if type(multiplicity) is not int:
            raise TypeError("'{}' must be an int".format(str(multiplicity)))

        return True

class Requirement(object):
    """This class defines a requirement"""

    _id_no = 0 #tk: need to fix id_no state; store all existing id_no's in a list?

    def __init__(self, modelName=None, txt=None, id=None):
        """Note: Requirement() class is intended for internal use by Model() class"""

        "Check if constructor arguments are valid"
        if self._isValidRequirementArgs(modelName, txt, id):
            pass

        """Stereotype"""
        self._stereotypes = set({'requirement'})

        """ID"""
        if id is None:
            Requirement._id_no += 1
            self._id = 'ID' + str(Requirement._id_no).zfill(3)
        else:
            self._id = 'ID' + str(id_no).zfill(3)

        """Name"""
        if modelName is None:
            Requirement._id_no += 1
            self._modelName = 'block' + str(Requirement._id_no)
        else:
            self._modelName = modelName

        """Text"""
        if txt is None:
            self.txt = ''
        else:
            self.txt = txt

        """UUID"""
        self._uuid = str(uuid.uuid1())

    def __repr__(self):
        _stereotypes = ""
        for _stereotype in self._stereotypes:
            _stereotypes += "\xab" + _stereotype + "\xbb "
        return _stereotypes + "\n{}".format(self._modelName)

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

    @staticmethod
    def _isValidRequirementArgs(modelName, txt, id):
        """Name"""
        if modelName is not None and type(modelName) is not str:
            raise TypeError("'{}' must be a string".format(str(modelName)))

        """Text"""
        if type(txt) is not str:
            raise TypeError("'{}' must be a string".format(str(txt)))

        """id"""
        if id is not None and type(id) not in [int, float, str]:
            raise TypeError("'{}' must be an int, float, or string".format(str(id)))

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

    _id_no = 0
    # _validStereotypes = set({'deriveReqt','refine','satisfy','verify'})

    def __init__(self, supplier, client, stereotype):
        if stereotype is 'deriveReqt':
            if type(supplier) is not Requirement:
                raise TypeError("'{}' is not a Requirement".format(str(supplier)))
            elif type(client) is not Requirement:
                raise TypeError("'{}' is not a Requirement".format(str(client)))
            else:
                self._supplier = supplier
                self._client = client
                self._stereotype = stereotype
        elif stereotype is 'satisfy':
            if type(supplier) is not Requirement:
                raise TypeError("'{}' is not a Requirement".format(str(supplier)))
            elif type(client) is not Block:
                raise TypeError("'{}' is not a Block".format(str(client)))
            else:
                self._supplier = supplier
                self._client = client
                self._stereotype = stereotype

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
    _validElements = [Block, Requirement, ConstraintBlock, Dependency]

    def __init__(self, modelName=None, elements={}):

        """Stereotype"""
        self._stereotypes = set({self.__class__.__name__.lower()})

        """Name"""
        if modelName is None:
            self.__class__._id_no += 1
            self._modelName = self.__class__.__name__ + str(self.__class__._id_no)
        elif type(modelName) is not str:
            raise TypeError("'{}' must be a string".format(str(modelName)))
        else:
            self._modelName = modelName

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
        return _stereotypes + "\n{}".format(self._modelName)

    @property
    def modelName(self):
        "Returns block modelName"
        return self._modelName

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

    def new_package(self, modelName=None, elements={}):
        """Creates a package element in model"""
        if modelName is None:
            key = _generateKey('package' + str(Package._id_no + 1))
        else:
            key = _generateKey(modelName)
        self._setElement(key, Package(modelName, elements))

    def new_block(self, modelName=None, typeName=None, parts={}, references=None, values={}, constraints={}, flowProperties=None, stereotypes=set(), multiplicity=1):
        """Creates a block element in package"""
        if modelName is None:
            key = _generateKey('package' + str(Package._id_no + 1))
        else:
            key = _generateKey(modelName)
        self._setElement(key, Block(modelName, typeName, parts, references, values, constraints, flowProperties, stereotypes, multiplicity))

    def new_requirement(self, modelName=None, txt=None):
        """Creates a requirement element in package"""
        if modelName is None:
            key = _generateKey('package' + str(Package._id_no + 1))
        else:
            key = _generateKey(modelName)
        self._setElement(key, Requirement(modelName, txt))

    def new_dependency(self, supplier, client, stereotype):
        """Creates a dependency element in package"""
        # element = Dependency(supplier, client, stereotype)
        key = _generateKey('dependency' + str(Dependency._id_no + 1))
        self._setElement(key, Dependency(supplier, client, stereotype))
        Dependency._id_no += 1

    def remove_element(self, key):
        """Removes a model element from package"""
        pass

    def RTM(self):
        """Generates a requirements traceability matrix for model elements contained and referenced within package"""
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

    def _setElement(self, key, element):
        # if key is None:
        #     key = _generateKey(element)
        if not self._isValidElement(type(element)):
            raise TypeError("'{}' is not a valid model element".format(str(element)))
        else:
            self._elements[key] = element

    def _isValidElement(self, modelElement):
        return modelElement in self._validElements or modelElement is Package

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
    # _validElements = set({Lifeline, Message, Occurence})

    def __init__(self, modelName=None, elements={}):

        """Stereotype"""
        self._stereotypes = set({"interaction"})

        """Name"""
        if modelName is None:
            self.__class__._id_no += 1
            self._modelName = self.__class__.__name__ + str(self.__class__._id_no)
        elif type(modelName) is not str:
            raise TypeError("'{}' must be a string".format(str(modelName)))
        else:
            self._modelName = modelName

        """Elements"""
        self._elements = elements

        """UUID"""
        self._uuid = str(uuid.uuid1())

    def __repr__(self):
        _stereotypes = ""
        for _stereotype in self._stereotypes:
            _stereotypes += "\xab" + _stereotype + "\xbb "
        return _stereotypes + "\n{}".format(self._modelName)

    @property
    def modelName(self):
        "Returns block modelName"
        return self._modelName

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
    def new_lifeline(self):
        pass

    ## Behavioral Diagrams
    def sd(self):
        """Generates a sequence diagram

        A sequence diagram represents the interaction between collaborating parts of a system.
        """
        pass

def _generateKey(modelName):
    """Generates a modeler-defined modelName for the given model element, and returns a string for use as a key within the modelNamespace of a parent model element."""
    if type(modelName) is not str:
        raise TypeError("'{}' is must be a string".format(str(modelName)))
    else:
        return modelName[0].lower() + modelName[1:].replace(' ','')
