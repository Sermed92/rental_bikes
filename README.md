# Rental Library

Rental is a library to model a rental bikes system. Here can be found the classes used to model the solution and the unit tests used to validate the code consistency.

# Design

The library was designed to keep the most simple approach, this way the result can be readable and easy to understand. Keeping in mind the principles for Python's design mentioned in the [Zen of Python](https://www.python.org/dev/peps/pep-0020/).

# Development

- Modular design
- Virtual environment
- Test driven
- Code refactoring
- Self describing classes, methods and properties

# Requirements

1. Is highly suggested to use a virtual environment with python 3.5 or higher.
2. Make sure you have pytest and pytest-cov installed.

# How to run test

Code coverage is up to 100%.

In case you have no pytest and/or pytest-cov, you can install it using pip:
    
    $ pip install -r test-requirements.txt

Now all you have to do is run the tests:

    $ pytest

To get code coverage you can run:

    $ pytest --cov=rental

