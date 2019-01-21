"""
Requirements display text-based requirements (and the requirements
specifications that contain them)
"""

from sysml.elements.base import ModelElement
from typing import Dict, List, Optional, Union


class Requirement(ModelElement):
    """This class defines a requirement"""

    def __init__(
        self, name: Optional[str] = "", txt: Optional[str] = "", id: Optional[str] = ""
    ):
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
