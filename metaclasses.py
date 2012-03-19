#!/usr/bin/python2.7

import logging


log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

######################################## simple class
class Car(object):
    brand = "audi"

    def __init__(self, model, doors_count=5):
        self.model = model
        self.doors_count = doors_count

    def go(self):
        log.info("driving %s %s with %s doors", self.brand, self.model, self.doors_count)

c = Car("a6")
c.go()


######################################## how to do that w/o shortcut
def go(self):
    log.info("driving %s %s with %s doors", self.brand, self.model, self.doors_count)

def init(self, model, doors_count=5):
    self.model = model
    self.doors_count = doors_count

attrs = {'__init__': init, 'go': go, 'brand': 'audi'}
superclasses = (object,)
Car2 = type("Car2", superclasses, attrs)

c2 = Car2("a6")
c2.go()

######################################## type is the top
assert type(c) == Car
assert type(Car) == type
assert type(type) == type

######################################## creating metaclass & using it
# metaclasses inherit from type

class Meta(type):
    pass

class Instance(object):
    __metaclass__ = Meta  # Python 2 only

######################################## can override __new__ and __init__
class MyMeta(type):

    def __new__(meta, name, supers, attrs):
        log.info("executing MyMeta new")
        return type.__new__(meta, name, supers, attrs)

    def __init__(cls, name,supers, attrs):
        log.info("executing MyMeta init")

class MyInstance(object):
    __metaclass__ = MyMeta

    def __init__(self):
        log.info("executing init in my instance")

# note that __new__ and __init__ from MyMeta are executed when
# MyInstance is created - not when instances are created
log.info("creating instances")
a1 = MyInstance()
a2 = MyInstance()
a3 = MyInstance()

######################################## mysterious class change
## You can return instance of another class from __new__

class Q(object):
    pass

class W(object):
    pass

class Other(Q, W):
    pass

class BaseChange(type):
    def __new__(meta, name, bases, attrs):
        log.info("meta = %s, name = %s, bases = %s, attrs = %s", meta, name, bases, attrs)
        return Other

class X(object):
    __metaclass__ = BaseChange

    def __init__(self):
        log.info("X init called")

    def foo(self):
        pass

x = X()
## X.__init__ is not called
# If __new__() does not return an instance of cls, then the new
# instance’s __init__() method will not be invoked.
log.info("class of x: %s", x.__class__)  # prints Other
log.info("superclasses of X: %s", x.__class__.__bases__)  # prints Q, W
