"""
Behavior of a system, in collaboration with its actors, can be described
by use cases, activities, interactions, and/or state machines.
"""

from sysml.elements.base import ModelElement
from sysml.elements.structure import Block
from collections import OrderedDict as _OrderedDict
from collections import Iterable
from typing import Dict, List, Optional, Union


class StateMachine(ModelElement):
    """This class defines a state"""

    def __init__(self, name: Optional[str] = ""):
        super().__init__(name)

    @property
    def name(self):
        return self._name


class Activity(ModelElement):
    """This class defines a activity"""

    def __init__(self, name: Optional[str] = ""):
        super().__init__(name)

    @property
    def name(self):
        return self._name


class Interaction(ModelElement):
    """This class defines an interaction"""

    def __init__(
        self,
        name: Optional[str] = "",
        lifelines: Optional[List["Block"]] = None,
        messages: Optional["ModelElement"] = None,
    ):
        super().__init__(name)

        self._lifelines: "_OrderedDict" = _OrderedDict()
        if lifelines is None:
            pass
        if isinstance(lifelines, Iterable):
            for lifeline in lifelines:
                if isinstance(lifeline, Block):
                    self._lifelines[lifeline.name] = lifeline
        else:
            raise TypeError

    @property
    def name(self):
        return self._name

    def add_lifeline(self, lifeline):
        if isinstance(lifeline, Block):
            self._lifelines[lifeline.name] = lifeline

    def remove_lifeline(self, lifeline):
        self._lifelines.pop(lifeline.name)
