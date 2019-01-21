"""
The `element.py` module contains all model elements that are valid for use by
the `model` class

---------

Model elements are the building blocks that make up SysML
"""

import uuid as _uuid
from abc import ABC as _ABC
from abc import abstractproperty as _abstractproperty
from typing import Optional


class ModelElement(_ABC):
    """Abstract base class for all model elements"""

    def __init__(self, name: Optional[str] = ""):
        if type(name) is str:
            self._name = name
        else:
            raise TypeError

        self._uuid = _uuid.uuid1()

    def __repr__(self):
        return "<{}('{}')>".format(self.__class__.__name__, self.name)

    @_abstractproperty
    def name(self):
        """Modeler-defined name of model element"""
        pass

    @property
    def stereotype(self):
        return "".join(
            [
                "\xab",
                self.__class__.__name__[0].lower(),
                self.__class__.__name__[1:],
                "\xbb",
            ]
        )

    @property
    def uuid(self):
        return self._uuid


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
