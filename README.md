# SysML.py

> A Python package for the Systems Modeling Language (SysML) - a general-purpose modeling language for systems engineering applications.

The design intent of this project is to provide an object-oriented programming (OOP) paradigm for model-based systems engineering.

[![Build Status](https://travis-ci.com/spacedecentral/SysML.py.svg?branch=dev)](https://travis-ci.com/spacedecentral/SysML.py)

## Package Overview

This python package consists of the following modules:

- `system.py` - contains the `Model()` class for instantiating `Model` objects, which serves as a central namespace for model elements (or relationships between elements).

- `element.py` - contains classes for instantiating *model element* objects (s.a., `Package`, `Block`, `Requirement`, `Activity`, etc.). These objects are intended for internal use by `Model` objects.

- `parser.py` - module for serializing/deserializing `Model` objects, using pickling.

## Developer Notes

This project is still in pre-alpha. For more details on current
milestone, please refer to
[#1](https://github.com/spacedecentral/SysML.py/issues/1).

## Contributing

1. Fork it (<https://github.com/yourusername/SysML.py/fork>)
2. Create your feature branch (`git checkout -b feature/logarithms`)
3. Commit your changes (`git commit -am 'Add some logarithms'`)
4. Push to the branch (`git push origin feature/logarithms`)
5. Create a new Pull Request
