# SysML.py

> A Python package for the Systems Modeling Language (SysML) - a general-purpose modeling language for systems engineering applications.

[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Build Status](https://travis-ci.com/spacedecentral/SysML.py.svg?branch=dev)](https://travis-ci.com/spacedecentral/SysML.py)
[![Coverage Status](https://coveralls.io/repos/github/spacedecentral/SysML.py/badge.svg)](https://coveralls.io/github/spacedecentral/SysML.py?branch=dev)

This project is intended to provide an object-oriented programming (OOP) paradigm for practicing Model-Based Systems Engineering (MBSE).

## Package Contents

- `sysml/system.py` - module for creating a `Model` object, which serves as a central namespace for model elements (and relationships between elements).

- `sysml/element.py` - module for creating model elements (s.a., `Package`, `Block`, `Requirement`, `Activity`, etc.). These objects are intended to be subsumed by a `Model` object, using a composite design pattern.

- `sysml/parser.py` - module for serializing/deserializing `Model` objects.

## Developer Notes

This project is still in pre-alpha. For a more detailed overview on design, usage, and features, please refer to
[#1](https://github.com/spacedecentral/SysML.py/issues/1).

Optional (but recommended for viewing GitHub issues): Install the [ZenHub for GitHub](https://chrome.google.com/webstore/detail/zenhub-for-github/ogcgkffhplmphkaahpmffcafajaocjbd?hl=en-US) chrome extension.

### Development Pipeline

The following semantic version names and corresponding features are being considered for the current development pipeline for `SysML.py`:

- `0.x.y` - standalone python package for SysML (coming soon to PyPI)
- `1.x.y` - to include features to support data interchange as per the current SysML (v1.5) specification
- `2.x.y` - to include features to support data interchange as per the upcoming SysML (v2.0) specification

## Contributing

1. Fork it (<https://github.com/yourusername/SysML.py/fork>)
2. Create your feature branch (`git checkout -b feature/logarithms`)
3. Commit your changes (`git commit -am 'Add some logarithms'`)
4. Push to the branch (`git push origin feature/logarithms`)
5. Create a new Pull Request
