#!/usr/bin/python2.7

## Does the same thing as string_find.py using regexes

import re

s = "hello world! Hello world"

## find
assert re.search(r"wor", s).start() == 6 # only first occurance
assert re.search(r"nemo", s) is None

all_wor = []
pos = -1
# must compile because re.search has no 'pos' argument
wor_re = re.compile(r"wor")
while True:
    g = wor_re.search(s, pos+1)
    if g is None:
        break
    else:
        pos = g.start()
    all_wor.append(pos)
assert all_wor == [6, 19]

## rsearch
# there is no rsearch function in re. You need to reverse the string
# and then apply re.search or re.RegexObject.search

## count
assert len(re.findall(r"w", s)) == 2
assert len(re.findall(r"z", s)) == 0
assert len(re.findall("aa", "aaaaaa")) == 3 # no overlapping

## replace
assert re.sub("world", "World", s) == "hello World! Hello World"
assert re.sub("world", "World", s, count=1) == "hello World! Hello world"
