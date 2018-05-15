============================
 SysML.py
============================

A Python package for the Systems Modeling Language (SysML) - a general-purpose modeling language for systems engineering applications.

The design intent of this project is to provide an object-oriented programming (OOP) paradigm for model-based systems engineering.

Package Overview
----------------
This python package consists of 3 modules:

- The ``system.py`` module contains the ``Model()`` class for creating *system model objects* to serve as a central repository for model elements (or relationships between elements), and provides instance methods for generating the 9 `SysML diagrams <http://sysmlforum.com/includes/what-are-sysml-diagram-types.html>`_.

- The ``elements.py`` module contains the *grammar* of SysML by providing classes for creating *model element objects* (e.g., package, block, constraintBlock, requirement, etc.). These objects are meant to be used internally by system model objects.

- The ``parser.py`` module contains a parser for importing SysML models from, or exporting to, a YAML file.

Developer Notes
---------------
This project is still in pre-alpha. For more details on current milestone, please refer to `#1 <https://github.com/spacedecentral/SysML.py/issues/1>`_.
