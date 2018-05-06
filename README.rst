============================
 SysML.py
============================

A Python package for the Systems Modeling Language (SysML) - a general purpose modeling language that supports analysis, design, and verification of complex systems.

The design intent of this project is to provide an object-oriented programming (OOP) paradigm for model-based systems engineering.

Package Overview
----------------
This python package primarily consists of 3 core modules:

- ``stereotypes.py`` contains the "grammar" of SysML by providing class objects for the core SysML "stereotypes" (e.g., «block», «requirement», «constraint», «refine», «satisfy», etc.).

- ``model.py`` contains the "Model" class for subsuming stereotypes into model elements or model relationships, and provides instance methods for generating the 9 SysML diagrams.

- ``parser.py`` contains a parser for importing SysML models from, or exporting to, a YAML file.

Developer Notes
---------------
This project is still in pre-alpha. For more details on current milestone, please refer to `#1 <https://github.com/spacedecentral/SysML.py/issues/1>`_.
