#!/usr/bin/python2.7
"""Copyright statement goes here
License goes here
Author goes here

This module presents how to use docstrigns according to google style
guide. It also demos that functions also have attributes.

You can use pydoc to see documentation for the file. You *must*
provide the modulename (filename w/o extension), otherwise you will
get "no Python documentation found for 'MODULENAME.py'" error

Using "pydoc -w" you can generate ugly-looking html page with docs

Pydoc will interpret your module. Use __name__ == "__main__" check to
avoid trouble
"""


def foo(greeting, rep=1):
    """Shows that even functions are objects in Python and how to
    format docstring.

    That's why you can access dostring as an attribute of a function.
    Docstrings usually have oneline showrt destription followed by
    empty line and longer description.Then you should see args, return
    values, returned/generated value and raised exceptions.

    You use foo.__doc__to access doc attribute of a funciton foo.

    Args:
        greeting: message printed by this funciton
        rep: how many times the greeting is repeated (all in separate
            lines). rep must be > 0

    Returns:
        number of bytes written to stdout

    Raises:
        AssertionError: rep must be positive
    """
    assert rep > 0
    for _ in xrange(rep):
        print greeting


class MyClass:
    """Shows that classes also have docstring

    Again, first line is short, then blank line followed by longer
    description
    """

    def __init__(self):
        """Methods get attributes in the same way as functions"""
        pass

if __name__ == "__main__":
    print "function docstring:", foo.__doc__
    print "class docstring:", MyClass.__doc__
    foo("hello world", rep=3)
