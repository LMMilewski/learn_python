#!/usr/bin/python2.7

def foo():
    pass

class C:
    pass

L = ["list", # string
     ["can", "mix"], # another list
     ("types",), # tuple
     1, # integer
     2.0, # float
     set(), dict(), # set and dict
     foo, C, sys] # function, class (not instance!), module

assert L[0] == "list"
assert L[1][1] == "mix"
assert L[-4] == dict() # negative indices start from the end
assert L[1:6:2] == [['can', 'mix'], 1, set()] # slicing: [FROM : TO : STEP]
assert range(5)[2:] == [2,3,4]
assert range(5)[:2] == [0,1]

L1 = []
L2 = L1
L1.append(0)
assert L2 == [0] # L2 is the same object as L1
L3 = L1[:] # same as L3 = list(L1)
L1.append(1)
assert L3 == [0] # L3 was a copy of L1 - thus now L1 != L3
assert L1 == [0,1]

L = []
L.append("hello")
assert L == ["hello"]
L += "world"
assert L == ["hello", "w", "o", "r", "l", "d"] # ouch!
L.extend([1,2,3,4])
assert L == ['hello', 'w', 'o', 'r', 'l', 'd', 1, 2, 3, 4]

L.insert(0, 1.0)
assert L == [1.0, 'hello', 'w', 'o', 'r', 'l', 'd', 1, 2, 3, 4]

assert len(L) == 11

## search
assert L.index("w") == 2
# L.index("qq") # rasies ValueError
assert "w" in L
assert "qq" not in L 

## remove
L = [1,1,1,2,2,3,3]
L.remove(2)
assert 2 in L
L.remove(2)
assert 2 not in L
# L.remove(2) # rasies ValueError
L = range(3)
assert L.pop() == 2
assert L == [0,1]


# multiply
L = ['w', 'q'] * 2
assert L == ['w', 'q', 'w', 'q']

L = [[0]]
L1 = L*3
L[0][0]=1
assert L1 == [[1], [1], [1]] # oops

