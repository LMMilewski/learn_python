#!/usr/bin/python2.7

x = 1, # tuple with one element (note the comma!)
y = 1, 2, 4, 5 # 4-element tuple
assert y[-1] == 5
assert y[2] == 4
assert y[1:3] == (2,4) # acts as a list, but does not create a list!
for yy in y:
    yy += 1 # we have a copy, we don't modify y
assert y == (1,2,4,5)
assert 2 in y
assert 10 not in y

a, b, c = [1,2,3]
assert a == 1 and b == 2 and c == 3
