"""
The `element.py` module contains all model elements that are valid for use by
the `model` class

---------

Model elements are the building blocks that make up SysML
"""

import uuid as _uuid
from abc import ABC as _ABC
from abc import abstractproperty as _abstractproperty
from pint import UnitRegistry as _UnitRegistry
_ureg = _UnitRegistry()


class ModelElement(_ABC):
    """Abstract base class for all model elements"""

    def __init__(self, name=''):
        if type(name) is str:
            self._name = name
        else:
            raise TypeError

        self._uuid = str(_uuid.uuid1())

    def __repr__(self):
        return "{} {}".format(self.stereotype, self.name)

    @_abstractproperty
    def name(self):
        """Modeler-defined name of model element"""
        pass

    @property
    def stereotype(self):
        return "".join(["\xab",
                        self.__class__.__name__[0].lower(),
                        self.__class__.__name__[1:],
                        "\xbb"
                        ])

    @property
    def uuid(self):
        return self._uuid


class ValueType(ModelElement):
    """This class defines a value type

    Parameters
    ----------
    units : str, default None

    Notes
    -----
    String parameter for units must be defined in the UnitRegistry

    Example
    -------
    >>> kesselrun = 12*sysml.ValueType('parsecs')
    >>> kesselrun
    \xabvalueType\xbb 'parsecs' [12]
    >>> kesselrun.magnitude
    12
    >>> kesselrun.units
    'parsec'
    >>> kesselrun.to('lightyear')
    \xabvalueType\xbb 'light_year' [39.138799173399406]
    """

    def __init__(self, units=None):
        # TODO: Needs to be redesigned to inherit methods of a UnitRegistry
        # object while also inheriting from ModelElement

        super().__init__(self.name)

    @property
    def name(self):
        return self._name


class Block(ModelElement):
    """This class defines a block

    Parameters
    ----------
    name : string, default None

    parts : dict, default None

    references : dict, default None

    values : dict, default None

    constraints : dict, default None

    flowProperties : dict, default None

    multiplicity : int, default 1

    """

    def __init__(self, name='', parts=None, references=None, values=None,
                 constraints=None, flowProperties=None, multiplicity=1):
        super().__init__(name)

        self._parts = dict()
        if parts is None:
            pass
        elif type(parts) is dict:
            for key, part in parts.items():
                if type(key) is str and isinstance(part, Block):
                    self_parts[key] = part
                else:
                    raise TypeError
        else:
            raise TypeError

        if references is None:
            self._references = dict()

        if values is None:
            self._values = dict()

        if constraints is None:
            self._constraints = dict()

        if flowProperties is None:
            self._flowProperties = dict()

        if isinstance(multiplicity, (int, float)):
            self._multiplicity = multiplicity
        else:
            raise TypeError
        """
        ## Reference Property
        if references is None:
            self._references = []
            elif type(references) is list:
            self._references = references
        else:
            raise TypeError("argument is not a list!")
        ## Flow Property
        if flows is None:
            self._flowProperties = dict()
        elif type(flowProperties) is dict:
            self._flowProperties = flowProperties
        else:
            raise TypeError("argument is not a dictionary!")
        ## Operations
        self.operations = []
        ## Constraints
        self.constaints = []
        """

    @property
    def name(self):
        return self._name

    @property
    def parts(self):
        return self._parts

    @property
    def references(self):
        return self._references

    @property
    def values(self):
        return self._values

    @property
    def constraints(self):
        return self._constraints

    @property
    def flows(self):
        return self._flowProperties

    @property
    def multiplicity(self):
        return self._multiplicity

    @name.setter
    def name(self, name):
        if type(name) is str:
            self._name = name
        else:
            raise TypeError

    @multiplicity.setter
    def multiplicity(self, multiplicity):
        if isinstance(multiplicity, (int, float)):
            self._multiplicity = multiplicity
        else:
            raise TypeError

    def add_part(self, partName, part):
        """Adds block element to parts attribute

        Parameters
        ----------
        partName : string

        block : Block

        """
        if type(partName) is str and isinstance(part, Block):
            self._parts[partName] = part
        elif type(partName) is not str:
            raise TypeError
        elif not isinstance(part, Block):
            raise TypeError

    def remove_part(self, partName):
        """Removes block element from parts attribute

        Parameters
        ----------
        partName : string

        """
        self._parts.pop(partName)

    def __getitem__(self, elementName):
        if type(elementName) is str:
            if elementName in self._parts.keys():
                return self._parts[elementName]
            elif elementName in self._references.keys():
                return self._references[elementName]
            elif elementName in self._values.keys():
                return self._values[elementName]
            elif elementName in self._constraints.keys():
                return self._constraints[elementName]
            elif elementName in self._flowProperties.keys():
                return self._flowProperties[elementName]
            else:
                raise KeyError
        else:
            raise TypeError

    def __setitem__(self, elementName, element):
        if type(elementName) is str and isinstance(element, Block):
            self._parts[elementName] = element
        elif type(elementName) is not str:
            raise TypeError
        elif not isinstance(element, Block):
            raise TypeError

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

    def __init__(self, name='', txt='', id=''):
        super().__init__(name)

        if type(txt) is str:
            self.txt = txt
        else:
            raise TypeError

        if type(id) is str:
            self._id = id
        else:
            raise TypeError

    @property
    def name(self):
        return self._name


class ConstraintBlock(ModelElement):
    """This class defines a constraint"""

    def __init__(self):
        super().__init__(name)


class Dependency(ModelElement):
    """A dependency relationship can be applied between models elements to
    indicate that a change in one element, the client, may result in a change
    in the other element, the supplier.

    Parameters
    ----------
    client : ModelElement

    supplier : ModelElement

    """

    def __init__(self, client, supplier):
        self._client = client
        self._supplier = supplier

        if not isinstance(client, ModelElement):
            raise TypeError
        if not isinstance(supplier, ModelElement):
            raise TypeError

        super().__init__()

    @property
    def name(self):
        return self._name

    @property
    def supplier(self):
        return self._supplier

    @property
    def client(self):
        return self._client


class DeriveReqt(Dependency):
    """The derive requirement relationship conveys that a requirement at the
    client end is derived from a requirement at the supplier end.

    Parameters
    ----------
    client : Requirement

    supplier : Requirement

    """

    def __init__(self, client, supplier):
        super().__init__(client, supplier)
        if type(client) is not Requirement:
            raise TypeError
        if type(supplier) is not Requirement:
            raise TypeError


class Satisfy(Dependency):
    """This relationship must have a requirement at the supplier end. SysML
    imposes no constraints on the kind of element that can appear at the client
    end. By convention, however, the client element is always a block

    Parameters
    ----------
    client : ModelElement

    supplier : Requirement

    Note
    ----
    A satisfy relationship assersion does not constitute proof. It is simply
    a mechanism to allocate a requirement to a structural element. Proof of
    satisfaction will come from test cases.

    See also
    --------
    Verify

    """

    def __init__(self, client, supplier):
        super().__init__(client, supplier)
        if type(supplier) is not Requirement:
            raise TypeError


class Package(ModelElement):
    """A package is a container for a set of model elements, of which may be
    other packages.

    Parameters
    ----------
    name : string, default None

    elements : dict, default None

    """

    def __init__(self, name='', elements=None):
        super().__init__(name)

        self._elements = dict()
        if elements is None:
            pass
        elif type(elements) is dict:
            for key, element in elements.items():
                if type(key) is str and isinstance(element, ModelElement):
                    self._elements[key] = element
                elif type(key) is not str:
                    raise TypeError
                elif not isinstance(element, ModelElement):
                    raise TypeError
        else:
            raise TypeError

    def __getitem__(self, elementName):
        "Returns elementName-specified model element"
        return self._elements[elementName]

    def __setitem__(self, elementName, element):
        "Sets elementName-specified model element"
        self._setElement(elementName, element)

    @property
    def name(self):
        return self._name

    @property
    def elements(self):
        return self._elements

    def add(self, elementName, element):
        """Adds a model element to package"""
        self._setElement(elementName, element)

    def remove(self, elementName):
        """Removes a model element from package"""
        self._elements.pop(elementName)

    def RTM(self):
        """Generates a requirements traceability matrix for model elements
        contained and referenced within package"""
        pass

    def _setElement(self, elementName, element):
        if type(elementName) is str and isinstance(element, ModelElement):
            self._elements[elementName] = element
        elif type(elementName) is not str:
            raise TypeError
        elif not isinstance(element, ModelElement):
            raise TypeError


class StateMachine(ModelElement):
    """This class defines a state"""

    def __init__(self):
        super().__init__(name)

    @property
    def name(self):
        return self._name


class Activity(ModelElement):
    """This class defines a activity"""

    def __init__(self):
        super().__init__(name)

    @property
    def name(self):
        return self._name


class Interaction(ModelElement):
    """This class defines an interaction"""

    def __init__(self, name='', lifelines=None, messages=None):
        super().__init__(name)

        self._lifelines = dict()
        if lifelines is None:
            pass
        elif isinstance(lifelines, Block):
            self._lifelines = lifelines

    @property
    def name(self):
        return self._name

    def add_lifeline(self, lifeline):
        if isinstance(lifeline, Block):
            self._lifelines[lifeline.name] = lifeline

    def remove_lifeline(self, lifeline):
        self._lifelines.pop(lifeline.name)
