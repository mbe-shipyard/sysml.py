"""
Diagrams

---------

SysML includes 9 types of diagrams, some of which are taken from UML.

-Block definition diagram
-Internal block diagram
-Package diagram
-Use case diagram
-Requirement diagram
-Activity diagram
-Sequence diagram
-State diagram
-Parametric diagram
"""

from sysmlpy.elements import *

## Structure
class BlockDefinitionDiagram(object):
    """This class defines a block definition diagram

    A block definition diagram describes the system hierarchy and system/component classifications.
    """

    def __init__(self, label=None, elements=None, relations=None):
        self._block_id_no = 0
        self._label = label
        self.block = {}
        self._relation = {}

    def __repr__(self):
        return "bdd[Package] {}".format(self.label)
    # Block Setters
    def new_block(self, label=None, values=None, parts=None, references=None, flowProperties=None):
        """ Instantiates a new \xabblock\xbb element within the bdd namespace.
        """
        # Block Label
        if label is None:
            self._block_id_no += 1
            _label = 'Block' + str(self._block_id_no)
            self.block[_label] = Block(_label)
        elif type(label) is str:
            _label = label
            self.block[_label] = Block(_label)
        elif label is not None:
            raise TypeError("argument is not a string!")
        ## Value Properties
        if type(values) is dict:
            self.block[_label]._values = values
        elif values is not None:
            raise TypeError("argument is not a dictionary!")
        ## Part Properties
        if type(parts) is list:
            self.block[_label]._parts = parts
        elif parts is not None:
            raise TypeError("argument is not a dictionary!")
        ## Reference Properties
        if type(references) is dict:
            self.block[_label]._references = references
        elif references is not None:
            raise TypeError("argument is not a dictionary!")
        ## Flow Properties
        if type(flowProperties) is dict:
            self.block[_label]._flowProperties = flowProperties
        elif flowProperties is not None:
            raise TypeError("argument is not a dictionary!")
        ## Operations
        self.operations = []
        ## Constraints
        self.constaints = []
    def add_blocks(self, *blocks):
        """ Adds existing \xabblock\xbb element within the bdd namespace.
        """
        for block in blocks:
            if type(block) is Block:
                self.block[block.label] = block

class InternalBlockDiagram(object):
    """This class defines an internal block diagram
    
    The internal block diagram describes the internal structure of a system in terms of its parts, ports, and connectors.
    """
    
    def __init__(self):
        pass

class PackageDiagram(object):
    """This class defines a package diagram

    The package diagram is used to organize the model.
    """

    def __init__(self):
        pass

## Behavior
class SequenceDiagram(object):
    """This class defines a sequence diagram

    A sequence diagram represents the interaction between collaborating parts of a system.
    """

    def __init__(self):
        pass

class StateDiagram(object):
    """This class defines a state machine diagram

    The state machine diagram describes the state transitions and actions that a system or its parts perform in response to events.
     """

    def __init__(self):
        pass

class ActivityDiagram(object):
    """This class defines an activity diagram

    The activity diagram represents the flow of data and control between activities.
    """

    def __init__(self):
        pass

class UseCaseDiagram(object):
    """This class defines a use case diagram

    A use-case diagram provides a high-level description of functionality that is achieved through interaction among systems or system parts.
    """

    def __init__(self):
        pass

## Requirements
class RequirementDiagram(object):
    """This class defines a requirement diagram

    The requirements diagram captures requirements hierarchies and requirements derivation, and the satisfy and verify relationships allow a modeler to relate a requirement to a model element that satisfies or verifies the requirements.
    """

    def __init__(self):
        pass

## Parametrics
class ParametricDiagram(object):
    """This class defines a parametric diagram

    The parametric diagram represents constraints on system property values such as performance, reliability, and mass properties, and serves as a means to integrate the specification and design models with engineering analysis models.
    """

    def __init__(self):
        pass

