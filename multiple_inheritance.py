#!/usr/bin/python2.7

## let's start with diamond problem

class A(object):
    def __init__(self):
        print "construct A"

    def foo(self):
        print "foo in A"

class B(A):
    def __init__(self):
        A.__init__(self)
        print "construct B"

    def foo(self):
        print "foo in B"

class C(A):
    def __init__(self):
        A.__init__(self)
        print "construct C"

    def foo(self):
        print "foo in C"

class D(B, C):
    def __init__(self):
        B.__init__(self)
        C.__init__(self)
        print "construct D"

d = D() # A is constructed twice - ABACD
A.foo(d) # foo in A
B.foo(d) # foo in B
C.foo(d) # foo in C
d.foo() # foo in B
# let's see what sits in MRO
print D.__mro__ # DBCA - see why foo was called from B? :-)


## using Class.__init__ directly in __init__ sux. You are better using
## super function
class AA(object):
    def __init__(self):
        print "construct AA"

    def foo(self):
        print "foo in AA"

class BB(AA):
    def __init__(self):
        super(BB, self).__init__()
        print "construct BB"

    def foo(self):
        print "foo in BB"

class CC(AA):
    def __init__(self): 
        super(CC, self).__init__()
        print "construct CC"

    def foo(self):
        print "foo in CC"

class DD(BB, CC):
    def __init__(self):
        super(DD, self).__init__() # syntax is different for Python3
        print "construct DD"

dd = DD()
print DD.__mro__

