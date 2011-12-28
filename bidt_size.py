#!/usr/bin/python2.7

## shows how many bytes you need to store dictionary


## dict
d = {}
last = d.__sizeof__()
print "Dict. Items: 0, Bytes: %s" % last
for i in xrange(65536):
    d[i] = i
    s = d.__sizeof__()
    if s != last:
        print "Dict. Items: %6d, Bytes: %8d, kB: %7.2f, MB: %4.2f" \
            % (i, s, s/1024.0, s/1024.0/1024.0)
        last = s

## list
print
L = []
last = L.__sizeof__()
print "List. Items: 0, Bytes: %s" % last
for i in xrange(65536):
    L.append(i)
    s = L.__sizeof__()
    if s != last:
        print "List. Items: %6d, Bytes: %8d, kB: %7.2f, MB: %4.2f" \
            % (i, s, s/1024.0, s/1024.0/1024.0)
        last = s

## set 
print
x = set()
last = x.__sizeof__()
print "Set. Items: 0, Bytes: %s" % last
for i in xrange(65536):
    x.add(i)
    s = x.__sizeof__()
    if s != last:
        print "Set. Items: %6d, Bytes: %8d, kB: %7.2f, MB: %4.2f" \
            % (i, s, s/1024.0, s/1024.0/1024.0)
        last = s
