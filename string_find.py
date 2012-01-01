#!/usr/bin/python2.7

s = "hello world! Hello world"

## find
assert s.find("wor") == 6 # only first occurance
assert s.find("nemo") == -1

all_wor = []
pos = -1
while True:
    pos = s.find("wor", pos+1)
    if pos == -1:
        break
    all_wor.append(pos)
assert all_wor == [6, 19]

## rfind
all_wor = []
pos = len(s)+1
while True:
    pos = s.rfind("wor", 0, pos-1)
    if pos == -1:
        break
    all_wor.append(pos)
assert all_wor == [19, 6]

## index/rindex - same as find/rfind, but raises ValueError on failure

## count
assert s.count("w") == 2
assert s.count("z") == 0
assert "aaaaaa".count("aa") == 3 # no overlapping

## replace
assert s.replace("world", "World") == "hello World! Hello World"
assert s.replace("world", "World", 1) == "hello World! Hello world"
