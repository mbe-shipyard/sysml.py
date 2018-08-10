"""
The `stereotype` module contains all model elements that are valid for use by the `model` class

---------

Model elements are the building blocks that make up the 9 SysML diagrams
"""

import uuid
from abc import ABC, abstractproperty

# developer notes: to use hidden vs unhidden attributes

class ModelElement(ABC):
    """Abstract base class for all model elements"""

    _id_no = 0

    def __init__(self, name=None):
        """UUID"""
        self._uuid = str(uuid.uuid1())

        """Name"""
        if name is None:
            self.__class__._id_no += 1
            self._name = self.__class__.__name__.lower() + str(self.__class__._id_no)
        elif type(name) is str:
            self._name = name
        else:
            raise TypeError("'{}' must be a string".format(str(name)))

    def __repr__(self):
        return ''.join(["\xab" + _stereotype + "\xbb\n" for _stereotype in self._stereotype]) + "{}".format(self.name)

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
        if type(name) is str:
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

    stereotype : set, default None

    multiplicity : int, default 1

    """

    def __init__(self, name=None, typeName=None, parts=None, references=None, values=None, constraints=None, flowProperties=None, stereotype=None, multiplicity=1):
        """Note: Block() class is intended for internal use by Model() class"""

        """Construct ModelElement"""
        super().__init__(name)

        """Stereotype"""
        self._stereotype = [self.__class__.__name__.lower()]
        if stereotype is None:
            pass
        elif type(stereotype) is str and stereotype not in self._stereotype:
            self._stereotype.append(stereotype)
        elif type(stereotype) is list:
            for stereotype in stereotype:
                if type(stereotype) is str:
                    self._stereotype.append(stereotype)
        else:
            raise TypeError("'{}' must be a string or set of strings".format(str(stereotype)))

        """Part Property"""
        self._parts = {}
        if parts is None:
            pass
        elif isinstance(parts, Block):
            self_parts[parts.name] = parts
        elif type(parts) is set:
            for part in parts:
                if isinstance(part, Block):
                    self_parts[part.name] = part
                else:
                    raise TypeError("'{}' must be a Block".format(str(part)))
        else:
            raise TypeError("'{}' must be a set".format(str(parts)))

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

    ## Getters
    @property
    def name(self):
        "Returns block name"
        return self._name

    @property
    def stereotype(self):
        return self._stereotype

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
        if type(name) is str:
            self._name = name
        else:
            raise TypeError("'{}' must be a string".format(str(name)))

    @multiplicity.setter
    def multiplicity(self, multiplicity):
        self._setMultiplicity(multiplicity)

    def add_part(self, block):
        """Adds block element to parts attribute"""
        if type(block) is Block:
            self._parts[block.name] = block
        else:
            raise TypeError("'{}' must be a Block".format(str(block)))

    def remove_part(self, block):
        """Removes block element from parts attribute"""
        self._parts.pop(block.name)

    def _setMultiplicity(self, multiplicity):
        if type(multiplicity) is int and multiplicity > 0:
            self._multiplicity = multiplicity
        elif type(multiplicity) is int:
            raise ValueError("'{}' must be a positive int".format(str(multiplicity)))
        else:
            raise TypeError("'{}' must be a positive int".format(str(multiplicity)))

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

class Requirement(ModelElement):
    """This class defines a requirement"""

    def __init__(self, name=None, txt=None, id=None):
        """Note: Requirement() class is intended for internal use by Model() class"""

        """Construct ModelElement"""
        super().__init__(name)

        """Stereotype"""
        self._stereotype = [self.__class__.__name__.lower()]

        """Text"""
        if txt is None:
            self.txt = ''
        elif type(txt) is str:
            self.txt = txt
        else:
            raise TypeError("'{}' must be a string".format(str(txt)))

        """ID"""
        if id is None:
            self.__class__._id_no += 1
            self._id = 'ID' + str(self.__class__._id_no).zfill(3)
        elif type(id) in [int, float, str]:
            self._id = 'ID' + str(id_no).zfill(3)
        else:
            raise TypeError("'{}' must be an int, float, or string".format(str(id)))

    @property
    def name(self):
        "Returns block name"
        return self._name

    @property
    def stereotype(self):
        return self._stereotype

class ConstraintBlock(ModelElement):
    """This class defines a constraint"""

    def __init__(self):

        """Construct ModelElement"""
        super().__init__(name)

class Dependency(ModelElement):
    """This class defines a dependency"""

    def __init__(self, supplier, client, stereotype):

        self._name = super()._generateKey(self.__class__.__name__.lower() + str(self.__class__._id_no + 1))
        if stereotype is 'deriveReqt':
            if type(supplier) is Requirement and type(client) is Requirement:
                self._supplier = supplier
                self._client = client
                self._stereotype = stereotype
            elif type(supplier) is not Requirement:
                raise TypeError("'{}' is not a Requirement".format(str(supplier)))
            elif type(client) is not Requirement:
                raise TypeError("'{}' is not a Requirement".format(str(client)))
        elif stereotype is 'satisfy':
            if type(supplier) is Block and type(client) is Requirement:
                self._supplier = supplier
                self._client = client
                self._stereotype = stereotype
            elif type(supplier) is not Block:
                raise TypeError("'{}' is not a Block".format(str(supplier)))
            elif type(client) is not Requirement:
                raise TypeError("'{}' is not a Requirement".format(str(client)))
        else:
            raise Exception("'{}' is not a valid dependency".format(str(stereotype)))

        """Construct ModelElement"""
        super().__init__(self._name)

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

    def __init__(self, name=None, elements=None):

        """Construct ModelElement"""
        super().__init__(name)

        """Stereotype"""
        self._stereotype = [self.__class__.__name__.lower()]

        """Elements"""
        self._elements = {}
        if elements is None:
            pass
        elif isinstance(elements, ModelElement):
            self._elements[element.name] = elements
        elif type(elements) is set:
            for element in elements:
                if isinstance(element, ModelElement):
                    self._elements[element.name] = element
                else:
                    raise TypeError("'{}' must be a valid model element".format(str(element)))
        else:
            raise TypeError("'{}' must be a valid model element or set of valid model elements".format(str(elements)))

    def __getitem__(self, key):
        "Returns model element for key-specified model element"
        return self._elements[key]

    def __setitem__(self, key, element):
        "Sets model element for key-specified model element"
        if isinstance(element, ModelElement):
            self._elements[key] = element
        else:
            raise TypeError("'{}' must be a valid model element".format(str(element)))

    @property
    def name(self):
        "Returns block name"
        return self._name

    @property
    def elements(self):
        return self._elements

    @property
    def stereotype(self):
        return self._stereotype

    def add(self, element):
        """Adds a model element to package"""
        if isinstance(element, ModelElement):
            self._elements[element.name] = element
        else:
            raise TypeError("'{}' must be a valid model element".format(str(element)))

    def remove(self, element):
        """Removes a model element from package"""
        self._elements.pop(element.name)

    def RTM(self):
        """Generates a requirements traceability matrix for model elements contained and referenced within package"""
        pass

class StateMachine(ModelElement):
    """This class defines a state"""

    def __init__(self):

        """Construct ModelElement"""
        super().__init__(name)

class Activity(ModelElement):
    """This class defines a activity"""

    def __init__(self):

        """Construct ModelElement"""
        super().__init__(name)

class Interaction(ModelElement):
    """This class defines an interaction"""

    def __init__(self, name=None, elements=None):

        """Construct ModelElement"""
        super().__init__(name)

        """Stereotype"""
        self._stereotype = self.__class__.__name__.lower()

        """Elements"""
        if elements is None:
            elements = {}
        self._elements = elements

    @property
    def name(self):
        "Returns block name"
        return self._name

    @property
    def elements(self):
        return self._elements

    @property
    def stereotype(self):
        return self._stereotype
