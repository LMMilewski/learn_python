#!/usr/bin/python2.7

import re

s = "hello world world"

## simple grouping examples
x = re.search(r"wor(.)(.?)(X?)|(NOMATCH)", s)
assert x.group() == "world"
assert x.groups() == ("l","d", '', None) # '' is because X? matches ''
assert x.group(4) is None # because group "NOMATCH" does not match
assert x.group(0, 2) == ("world", "d")

## you can name groups
# group 'hello_gr' matches hello
# group 'world_gr' matches world
x = re.search(r"(?P<hello_gr>hello)|(?P<world_gr>world)", s)
assert x.group("hello_gr") == "hello"
assert x.group("world_gr") is None
assert x.groups() == ("hello", None)
# groupdict works only for named patterns
assert x.groupdict() == {'world_gr': None, 'hello_gr': 'hello'}

## if pattern matches multiple times then last match is returned
x = re.search(r"(\d)*", "12")
assert x.group(0, 1) == ("12", "2")


## expand (subsitution using matched groups)
# using group ids
x = re.match(r"Name: (\w+) (\w+)", "Name: Lukas Milewski")
y = x.expand(r"Last name: \2\nFirst Name: \1")
assert y == "Last name: Milewski\nFirst Name: Lukas"

# using group names
x = re.match(r"Name: (?P<name>\w+) (?P<surname>\w+)", "Name: Lukas Milewski")
y = x.expand(r"Last name: \g<surname>\nFirst Name: \g<name>")
assert y == "Last name: Milewski\nFirst Name: Lukas"
