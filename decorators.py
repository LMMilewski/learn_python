#!/usr/bin/python2.7

import logging
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)


################################################################################ Simple example
# Property decorator is very common decorator from standard library
class A(object):

    @property
    def value(self):
        return 1

    # value = property(value)  # using @property is equivalent to this call

a = A()
log.info("property 'value': [%s]", a.value)


################################################################################ Adding flags to functions

# decorator that marks function as exposed
def expose(func):
    func.exposed = True
    return func

@expose
def myfun():
    return 1

log.info("myfun is exposed: %s", myfun.exposed)


################################################################################ Passing args to decorators
# You can't do that, but you can define function that takes argument
# and returns decorator based on the argument

def add_header(header):
    def add_header(func):
        func.header = header
        func.exposed = True
        return func
    return add_header

@add_header("decorated function")
def foo():
    return 1

log.info("foo exposed %s, foo header [%s]", foo.exposed, foo.header)


################################################################################ Changing function
# Decorator can return any function you want. For example you can
# write decorator that memoizes values returned by the function

def memoize(func):
    def func_with_caching(*args):
        if not hasattr(func, "cache"):
            func.cache = {}
        if args not in func.cache:
            func.cache[args] = func(*args)
        return func.cache[args]
    return func_with_caching

@memoize
def computation(n):
    """Doc string"""
    log.info("Heavy computations for %s", n)
    return 1

computation(0)
computation(0)
computation(0)
computation(0)
computation(1)


################################################################################ Doc strings etc.
# Unfortunately that messes up doc strings. You can take care of that
# in the decorator if you want though
assert computation.__doc__ is None


################################################################################ Decorating class
from functools import total_ordering

@total_ordering
class B(object):
    def __eq__(self, other):
        return True

    def __lt__(self, other):
        return True

a = B()
b = B()
log.info("a > b: %s", a > b)  # can compare even though we didn't define '>'
