"""
The `element.py` module contains all model elements that are valid for use by
the `model` class

---------

Model elements are the building blocks that make up SysML
"""

from sysml.elements.base import ModelElement
from typing import Dict, List, Optional, Union


class Requirement(ModelElement):
    """This class defines a requirement"""

    def __init__(self, name="", txt="", id=""):
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
