#!/usr/bin/env python

"""Test demo 7.2 for chapter 7."""

from copy import deepcopy

s = set('cheeseshop')
t = frozenset('bookshop')

print s == t
print s != t
print ''

u = frozenset(s)
print s == u

print set('posh') == set('shop')
print ''

print s ^ t == s.symmetric_difference(t)
print ''

v = s
v |= t
print v
print ''

w = s.copy()
x = deepcopy(s)
print id(s)
print s
print id(w)
print w
print id(x)
print x
print ''

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
