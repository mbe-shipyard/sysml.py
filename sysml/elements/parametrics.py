"""
Parametric are used to express how one or more constraints — specifically,
equations and inequalities — are bound to the properties of a system.
Parametrics support engineering analyses, including performance, reliability,
availability, power, mass, and cost. Parametrics can also be used to support
trade studies of candidate physical architectures.
"""

from sysml.elements.base import ModelElement
from pint import UnitRegistry as _UnitRegistry
from typing import Optional
from pint import UnitRegistry as _UnitRegistry

_u = _UnitRegistry()


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
    <ValueType(12, 'parsecs')>
    >>> kesselrun.magnitude
    12
    >>> kesselrun.units
    <Unit('parsec')>
    >>> kesselrun.to('lightyear')
    <ValueType(39.138799173399406, 'light_year')>
    """

    def __init__(self, units: Optional[str] = ""):

        super().__init__(self.name)

    @property
    def name(self):
        return self._name


class ConstraintBlock(ModelElement):
    """This class defines a constraint"""

    def __init__(self, name: Optional[str] = ""):
        super().__init__(name)
