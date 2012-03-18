#!/usr/bin/python2.7

import logging
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)


######################################## File example
## Without 'with' you have no guarantee when Python will close the
## file (note that CPython at this moment closes the file immediately
## after it goes out of scope, but that's something that might change)
##
## 'with' guarantees that you get close the file just after with block
## even if there are exceptions thrown
with open("/etc/passwd") as f:
    for line in f:
        log.info("%s", line.split(":")[0])


######################################## Context manager is a class
## Our context manager will make sure that our changes to a list
## variable are reverted after we leave 'with' block
import copy

class ref_jail(object):
    def __init__(self, var):
        self.var = var
        self.orig_value = copy.copy(var)

    def __enter__(self):
        return self.var

    def __exit__(self, exc_type, exc_val, exc_traceback):
        while self.var:
            self.var.pop()
        self.var.extend(self.orig_value)
    
g_list = [1,2,3]
log.info("list before with: %s", g_list)
try:
    with ref_jail(g_list) as L:
        L.extend([1,2,3,4])
        log.info("extended list: %s", g_list)
        raise RuntimeError("hello")
except:
    log.info("after with: %s", g_list)

######################################## other way
## Same thing but using contextlib (and you get a little bit different
## syntax for 'with')
import contextlib
import copy

@contextlib.contextmanager
def ref_jail_2(var):
    orig_var = copy.copy(var)
    try:
        yield
    finally:
        while(var):
            var.pop()
        var.extend(orig_var)

g_list = [1,2,3]
log.info("list before with: %s", g_list)
try:
    with ref_jail_2(g_list):  # note the difference! we don't have 'as X'
        g_list.extend([1,2,3,4])
        log.info("extended list: %s", g_list)
        raise RuntimeError("hello")
except:
    log.info("after with: %s", g_list)
