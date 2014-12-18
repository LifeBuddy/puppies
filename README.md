puppies
======
Professionals directory by tag and location

[![Build Status](http://img.shields.io/travis/astronouth7303/puppies/master.svg)](https://travis-ci.org/astronouth7303/puppies)
[![Coverage Status](http://img.shields.io/coveralls/astronouth7303/puppies/master.svg)](https://coveralls.io/r/astronouth7303/puppies)
[![Scrutinizer Code Quality](http://img.shields.io/scrutinizer/g/astronouth7303/puppies.svg)](https://scrutinizer-ci.com/g/astronouth7303/puppies/?branch=master)
[![PyPI Version](http://img.shields.io/pypi/v/puppies.svg)](https://pypi.python.org/pypi/puppies)
[![PyPI Downloads](http://img.shields.io/pypi/dm/puppies.svg)](https://pypi.python.org/pypi/puppies)


Getting Started
===============

Requirements
------------

* Python 3.3+

Installation
------------

puppies can be installed with pip:

```
$ pip install puppies
```

or directly from the source code:

```
$ git clone https://github.com/astronouth7303/puppies.git
$ cd puppies
$ python setup.py install
```

Basic Usage
===========

After installation, abstract base classes can be imported from the package:

```
$ python
>>> import puppies
puppies.__version__
```

puppies doesn't do anything, it's a template.

For Contributors
================

Requirements
------------

* Make:
    * Windows: http://cygwin.com/install.html
    * Mac: https://developer.apple.com/xcode
    * Linux: http://www.gnu.org/software/make (likely already installed)
* virtualenv: https://pypi.python.org/pypi/virtualenv#installation
* Pandoc: http://johnmacfarlane.net/pandoc/installing.html
* Graphviz: http://www.graphviz.org/Download.php

Installation
------------

Create a virtualenv:

```
$ make env
```

Run the tests:

```
$ make test
$ make tests  # includes integration tests
```

Build the documentation:

```
$ make doc
```

Run static analysis:

```
$ make pep8
$ make pep257
$ make pylint
$ make check  # includes all checks
```

Prepare a release:

```
$ make dist  # dry run
$ make upload
```
