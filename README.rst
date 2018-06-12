============================
 SysML.py
============================
.. image:: https://travis-ci.com/spacedecentral/SysML.py.svg?branch=dev
    :target: https://travis-ci.com/spacedecentral/SysML.py

A Python package for the Systems Modeling Language (SysML) - a general-purpose modeling language for systems engineering applications.

The design intent of this project is to provide an object-oriented programming (OOP) paradigm for model-based systems engineering.

Package Overview
----------------
This python package consists of the following modules:

- The ``system.py`` module contains the ``Model()`` class for instantiating ``Model`` objects, which serves as a central namespace for model elements (or relationships between elements).

- The ``element.py`` module contains classes for instantiating *model element* objects (s.a., ``Package``, ``Block``, ``Requirement``, ``Activity``, etc.). These objects are intended for internal use by ``Model`` objects.

Developer Notes
---------------
This project is still in pre-alpha. For more details on current milestone, please refer to `#1 <https://github.com/spacedecentral/SysML.py/issues/1>`_.
