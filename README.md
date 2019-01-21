# SysML.py

> A Python package for the Systems Modeling Language (SysML)

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Build Status](https://travis-ci.com/spacedecentral/SysML.py.svg?branch=dev)](https://travis-ci.com/spacedecentral/SysML.py)
[![Coverage Status](https://coveralls.io/repos/github/spacedecentral/SysML.py/badge.svg)](https://coveralls.io/github/spacedecentral/SysML.py?branch=dev)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

**SysML.py** is an open source, Apache-licensed library providing a [Python](https://www.python.org) implementation of the [Systems Modeling Language](https://sysml.org) (SysML) for practicing [Model-Based Systems Engineering](https://www.incose.org/docs/default-source/delaware-valley/mbse-overview-incose-30-july-2015.pdf) (MBSE).

## Package Contents

- `sysml/system.py` - module for creating a `Model` object, which serves as a central namespace for model elements (and relationships between elements).

- `sysml/elements/` - modules for creating model elements, divided into 4 pillars: structure, behavior, requirements, and parametrics. These objects are intended to be subsumed by a `Model` object.

## Developer Notes

This project is still in pre-alpha. For a more detailed overview on design, usage, and features, please refer to
[Design considerations for initial package release](https://github.com/spacedecentral/SysML.py/issues/1).

### Development Pipeline

The following [semver](https://semver.org/) releases are being considered for the development pipeline for SysML.py:

- `0.x.y` - a standalone python implementation of SysML
- `1.x.y` - a full profile implementation of the current SysML ([v1.5](https://sysml.org/docs/specs/OMGSysML-v1.5-17-05-01.pdf)) specification
- `2.x.y` - a full profile implementation of the upcoming SysML ([v2.0](https://www.phoenix-int.com/wp-content/uploads/2018/05/Phx2018UC_KEYNOTE_Friedenthal.pdf)) specification

## Contributing

Optional (but recommended for viewing GitHub issues): Install the [ZenHub for GitHub](https://chrome.google.com/webstore/detail/zenhub-for-github/ogcgkffhplmphkaahpmffcafajaocjbd?hl=en-US) chrome extension.

1. Fork it (<https://github.com/yourusername/SysML.py/fork>)
2. Create your feature branch (`git checkout -b feature/logarithms`)
3. Commit your changes (`git commit -am 'Add some logarithms'`)
4. Push to the branch (`git push origin feature/logarithms`)
5. Create a new Pull Request
