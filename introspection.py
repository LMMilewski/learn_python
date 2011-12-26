#!/usr/bin/python2.7

## functions
def foo():
    """hello world from docstring"""
    x = 1
    return lambda: x
print "function foo dir", foo.__doc__
f = foo()
print "function f dir", dir(f)
print "f closure", f.__closure__

## modules
print "sys module dir:", dir(sys)

## classes
class A():
    def __init__(self):
        self.x = 1

    def foo(self):
        self.y = 2

print "class A dir:", dir(A)
a = A()
print "instance of class A dir:", dir(a)
a.foo()
print "instance of class A dir after foo:", dir(a)

## if the object provides __dir__ method then it is used to return
## list of attributes
class C(object): # you *MUST* inherit object for this to work
    # it seems that usually you should inherit object
    def __dir__(self):
        return ["hello", "from", "my", "__dir__"]
print "class C dir", dir(C) # will work as usuall
c = C()
print "instance of class C dir", dir(c) # returns sorted(["hello", "from", "my", "__dir__"])


## get list of methods
print "Methods in A"
for m in dir(A):
    if callable(getattr(A, m)):
        print m

print "Methods in instance of A"
aa = A()
for m in dir(aa):
    if callable(getattr(aa, m)):
        print m

