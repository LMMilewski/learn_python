#!/usr/bin/python2.7

class A(object): pass
class B(object):pass
class C(A, B): pass
class D(B, A): pass
# class E(C, D): pass # raises exception ;-)
