#!/usr/bin/python2.7


class A(object):

    def foo(self):
        print "foo in A"
        return self.bar()

    def bar(self):
        print "bar in A"
        return 1

class B(A):

    def bar(self):
        print "bar in B"
        return 2


b = B()
assert b.foo() == 2 # bar in B

a = A()
assert a.foo() == 1 # bar in A

