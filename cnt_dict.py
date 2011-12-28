#!/usr/bin/python2.7

## you can inherit built-in data types - say dict

class CntDict(dict):

    def __init__(self):
        self.cnt = 0

    def get_cnt(self):
        return self.cnt

    def __setitem__(self, var, val):
        if var not in self:
            self.cnt += 1
        super(CntDict, self).__setitem__(var, val)

    def __delitem__(self, var):
        self.cnt -= 1
        super(CntDict, self).__delitem__(var)

    def update(self, d):
        for k, v in d.iteritems():
            self[k] = v

    def __len__(self):
        return self.get_cnt()

d = CntDict()
d[0] = 0
d[1] = 1
d[1] = 2
d[1] = 3
d[0] = 1
d[2] = 2
d[2] = 2
print d.get_cnt()
assert d.get_cnt() == 3

del d[0]
assert d.get_cnt() == 2
del d[1]
assert d.get_cnt() == 1
del d[2]
assert d.get_cnt() == 0

d[100] = 100
d[101] = 101
assert d.get_cnt() == 2
d.update(dict([(x, x) for x in xrange(5)]))
assert d.get_cnt() == 2+5

