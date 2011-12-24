#!/usr/bin/python2.7

d1 = {1:"one", 2:"two", 3:"three"}
d1[4] = "four"
assert 1 in d1
assert 5 not in d1
assert d1[3] == "three" 

d2 = dict([(v, k) for k, v in d1.iteritems()]) # NOTE iteritems call!
assert d2["two"] == 2
# d2["Two"] # that raises KeyError as keys are case sensitive

# you can mix types on left hand side as well as right hand side
two = {"string": "two", "int": 2, "float": 2.0, 2: "2", (0,0): "unknown tuple"}
assert two["string"] == "two"
assert two["int"] == 2
assert two["float"] == 2.0
assert two[2] == "2"
assert two[0, 0] == "unknown tuple"
# but since dict is implemented using hash table (yeah, implementation
# leaks in the interface) you can't use list/dict/set as a key (these
# are not hashable). You would get TypeError: unhashable type.
# 
# These won't work:
# two[dict()] = 1
# two[set()] = 2
# two[list()] = 3

# You can also delete items from dict
assert 2 in two
del two[2]
assert 2 not in two

assert "int" in two
two.clear()
assert "int" not in two

# check size
assert len(d1) == 4
