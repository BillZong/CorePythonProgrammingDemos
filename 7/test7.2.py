#!/usr/bin/env python

"""Test demo 7.2 for chapter 7."""

print set()
print set([])
print set(())
print ''

t = frozenset(['abc', 'efg'])
print t
print len(t)
print 'abc' in t
print ''

f = open('numbers', 'w')
for i in range(5):
    f.write('%d\n' % i)

f.close()
f = open('numbers', 'r')
print set(f)
f.close()
