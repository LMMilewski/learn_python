#!/usr/bin/python2.7

import re
x = re.sub(r"\w+", lambda x: 2*x.group(), "hello world")
assert x == "hellohello worldworld"
