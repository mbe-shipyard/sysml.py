"""
The `stereotypes` module contains all model elements that are valid for use by the `model` class

---------

Model elements are the building blocks that make up the 9 SysML diagrams
"""

import uuid
from abc import ABC, abstractproperty

# developer notes: to use hidden vs unhidden attributes

class ModelElement(ABC):
    """Abstract base class for all model elements"""

    def __init__(self):
        """UUID"""
        self._uuid = str(uuid.uuid1())

    @abstractproperty
    def name(self):
        """Modeler-defined name of model element"""
        pass

    @property
    def uuid(self):
        return self._uuid

    @staticmethod
    def _generateKey(name):
        """Takes a modeler-defined name and returns a formatted string for use as a key within the namespace of a parent model element"""
        if type(name) is not str:
            raise TypeError("'{}' is must be a string".format(str(name)))
        else:
            return name[0].lower() + name[1:].replace(' ','')

class Block(ModelElement):
    """This class defines a block

    Parameters
    ----------
    name : string, default None

    typeName : string, default None

    parts : dict, default None

    references : list, default None

    values : dict, default None

    constraints : dict, default None

    flowProperties : dict, default None

    stereotypes : set, default None

    multiplicity : dict, default 1

    """

    _id_no = 0 #tk: need to fix id_no state; store all existing id_no's in a list?

    def __init__(self, name=None, typeName=None, parts=None, references=None, values=None, constraints=None, flowProperties=None, stereotypes=None, multiplicity=1):
        """Note: Block() class is intended for internal use by Model() class"""

        "Check if constructor arguments are valid"
        if self._isValidBlockArgs(name, typeName, parts, references, values, constraints, flowProperties, stereotypes, multiplicity):
            pass

        """Construct ModelElement"""
        super().__init__()

        """Stereotype"""
        if stereotypes is None:
            stereotypes = set()
        self._stereotypes = set({'block'}).union(stereotypes)

        """Name"""
        if name is None:
            Block._id_no += 1
            self._name = 'block' + str(Block._id_no)
        else:
            self._name = name

        """Part Property"""
        if parts is None:
            self._parts = {}

        """Value Property"""
        if values is None:
            self._values = {}

        """Constraint Property"""
        if constraints is None:
            self._constraints = {}

        """Multiplicity"""
        self._setMultiplicity(multiplicity)

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
            raise TypeError("'{}' must be a string".format(str(name)))
        else:
            self._name = name

    @multiplicity.setter
    def multiplicity(self, multiplicity):
        self._setMultiplicity(multiplicity)

    def add_part(self, *blocks):
        """Adds any number of block elements to parts attribute"""
        for block in blocks:
            if type(block) is not Block:
                raise TypeError("'{}' must be a Block".format(str(block)))
        for block in blocks:
            key = block.name
            self._parts[key] = block

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
    def _isValidBlockArgs(name, typeName, parts, references, values, constraints, flowProperties, stereotypes, multiplicity):
        """Stereotype"""
        if stereotypes is not None and type(stereotypes) is not set:
            raise TypeError("'{}' must be a string or set of strings".format(str(stereotypes)))
        elif type(stereotypes) is set:
            for stereotype in stereotypes:
                if type(stereotype) is not str:
                    raise TypeError("'{}' must be a string".format(str(stereotype)))

        """Name"""
        if name is not None and type(name) is not str:
            raise TypeError("'{}' must be a string".format(str(name)))

        """Part Property"""
        if parts is not None and type(parts) is not dict:
            raise TypeError("'{}' must be a dict".format(str(parts)))
        elif type(parts) is dict:
            for key in parts:
                if type(key) is not str:
                    raise TypeError("'{}' must be a string".format(str(key)))
                elif not isinstance(parts[key], Block): #tk: change to accept block or list of blocks
                    raise TypeError("'{}' must be a Block".format(str(part[key])))

        """Value Property"""
        if values is not None and type(values) is not dict:
            raise TypeError(str(values) + " must be a dict")
        elif type(values) is dict:
            for key in values:
                if type(key) is not str:
                    raise TypeError("'{}' must be a string".format(str(key)))
                elif type(values[key]) is not int or type(values[key]) is not float or not hasattr(values[key],'units'):
                    raise TypeError("'{}' must be an int, float, or have attribute 'unit'".format(str(values[key])))

        """Constraint Property"""
        if constraints is not None and type(constraints) is not dict:
            raise TypeError(str(constraints) + " must be a dict")
        elif type(constraints) is dict:
            for key in constraints:
                if type(key) is not str:
                    raise TypeError("'{}' must be a string".format(str(key)))
                if not isinstance(constraints[key], ConstraintBlock):
                    raise TypeError("'{}' must be a ConstraintBlock".format(str(constraints[key])))

        """Multiplicity"""
        if multiplicity is not None and type(multiplicity) is not int:
            raise TypeError("'{}' must be an int".format(str(multiplicity)))

        return True

class Requirement(ModelElement):
    """This class defines a requirement"""

    _id_no = 0 #tk: need to fix id_no state; store all existing id_no's in a list?

    def __init__(self, name=None, txt=None, id=None):
        """Note: Requirement() class is intended for internal use by Model() class"""

        "Check if constructor arguments are valid"
        if self._isValidRequirementArgs(name, txt, id):
            pass

        """Construct ModelElement"""
        super().__init__()

        """Stereotype"""
        self._stereotypes = set({'requirement'})

        """ID"""
        if id is None:
            Requirement._id_no += 1
            self._id = 'ID' + str(Requirement._id_no).zfill(3)
        else:
            self._id = 'ID' + str(id_no).zfill(3)

        """Name"""
        if name is None:
            Requirement._id_no += 1
            self._name = 'requirement' + str(Requirement._id_no)
        else:
            self._name = name

        """Text"""
        if txt is None:
            self.txt = ''
        else:
            self.txt = txt

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
    def stereotypes(self):
        return self._stereotypes

    @staticmethod
    def _isValidRequirementArgs(name, txt, id):
        """Name"""
        if name is not None and type(name) is not str:
            raise TypeError("'{}' must be a string".format(str(name)))

        """Text"""
        if type(txt) is not str:
            raise TypeError("'{}' must be a string".format(str(txt)))

        """id"""
        if id is not None and type(id) not in [int, float, str]:
            raise TypeError("'{}' must be an int, float, or string".format(str(id)))

class ConstraintBlock(ModelElement):
    """This class defines a constraint"""

    def __init__(self):

        """Construct ModelElement"""
        super().__init__()

class Dependency(ModelElement):
    """This class defines a dependency"""

    _id_no = 0

    def __init__(self, supplier, client, stereotype):

        self._name = super()._generateKey('dependency' + str(Dependency._id_no + 1))
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

        """Construct ModelElement"""
        super().__init__()

    @property
    def name(self):
        "Returns block name"
        return self._name

    @property
    def supplier(self):
        return self._supplier

    @property
    def client(self):
        return self._client

    @property
    def stereotype(self):
        return self._stereotype

class Package(ModelElement):
    """This class defines a package"""

    _id_no = 0
    _validElements = [Block, Requirement, ConstraintBlock, Dependency]

    def __init__(self, name=None, elements=None):

        """Construct ModelElement"""
        super().__init__()

        """Stereotype"""
        self._stereotypes = set({self.__class__.__name__.lower()})

        """Name"""
        if name is None:
            self.__class__._id_no += 1
            self._name = self.__class__.__name__ + str(self.__class__._id_no)
        elif type(name) is not str:
            raise TypeError("'{}' must be a string".format(str(name)))
        else:
            self._name = name

        """Elements"""
        if elements is None:
            elements = {}
        self._elements = elements

    def __getitem__(self, key):
        "Returns model element for key-specified model element"
        return self._elements[key]

    def __setitem__(self, key, element):
        "Sets model element for key-specified model element"
        if not self._isValidElement(type(element)):
            raise TypeError("'{}' must be a valid model element".format(str(element)))
        self._elements[key] = element

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

    def add(self, *elements):
        """Adds any number of model elements to package"""
        for element in elements:
            if not self._isValidElement(type(element)):
                raise TypeError("'{}' must be a valid model element".format(str(element)))
        for element in elements:
            key = element.name
            self._elements[key] = element

    def remove(self, key):
        """Removes a model element from package"""
        self._elements.pop(key)

    def RTM(self):
        """Generates a requirements traceability matrix for model elements contained and referenced within package"""
        pass

    def _isValidElement(self, modelElement):
        return modelElement in self._validElements or modelElement is Package

class StateMachine(ModelElement):
    """This class defines a state"""

    def __init__(self):

        """Construct ModelElement"""
        super().__init__()

class Activity(ModelElement):
    """This class defines a activity"""

    def __init__(self):

        """Construct ModelElement"""
        super().__init__()

class Interaction(ModelElement):
    """This class defines an interaction"""

    _id_no = 0
    # _validElements = set({Lifeline, Message, Occurence})

    def __init__(self, name=None, elements=None):

        """Construct ModelElement"""
        super().__init__()

        """Stereotype"""
        self._stereotypes = set({"interaction"})

        """Name"""
        if name is None:
            self.__class__._id_no += 1
            self._name = self.__class__.__name__ + str(self.__class__._id_no)
        elif type(name) is not str:
            raise TypeError("'{}' must be a string".format(str(name)))
        else:
            self._name = name

        """Elements"""
        if elements is None:
            elements = {}
        self._elements = elements

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
