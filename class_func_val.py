#!/usr/bin/python2.7

## functions

def identity(x):
    return x
    
def foo(x, f=identity): # f: functions as arguments
    def bar(y):
        return f(y + x)
    return bar # bar: functions returned by value

f = foo(5)
assert f(1) == 6
assert f(2) == 7

g = foo(10, lambda x: 2*x)
assert g(1) == 22
assert g(2) == 24


# The following does not work. Seems that python has read-only clojures

# def make_cnt():
#     c = 0
#     def cnt():
#         c += 1 
#         return c
#     return cnt

# c = make_cnt()
# assert c() == 1
# assert c() == 2
# assert c() == 3

# d = make_cnt()
# assert d() == 1
# assert d() == 2
# assert d() == 3



## classes

class a(object):
    def up(self):
        return 'A'

class b(object):
    def up(self):
        return "B"

class c(object):
    def up(self):
        return "C"

class unknown(object):
    def up(self):
        return "?"
    

def char_uper(ch):
    import class_func_val
    if hasattr(class_func_val, ch):
        return getattr(class_func_val, ch) # return class, not instance!
    else:
        return unknown

def test(uper, exp_ch): # uper - pass class as argument
    return uper().up() == exp_ch

assert test(char_uper('a'), 'A')
assert test(char_uper('b'), 'B')
assert test(char_uper('c'), 'C')
assert test(char_uper('d'), '?')
