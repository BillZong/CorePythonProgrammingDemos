#!/usr/bin/env python

"""Test demo 7.1 for chapter 7."""

s = set('cheeseshop')
print s

t = frozenset('bookshop')
print t

print type(s)
print type(t)

print len(s)
print len(t)
print s == t
print ''

if s <= t:
    print "s is t's subset."
else:
    print "s isn't t's subset."

if s >= t:
    print "s is t's superset."
else:
    print "s isn't t's superset."

print "s and t's intersection is %s" % (s & t)
print "s and t's union is %s" % (s | t)
print "s's relative complement in t is %s" % (t - s)
print "t's relative complement in s is %s" % (s - t)
print "s and t's symmetric differennce is %s" % (s ^ t)
print ""

print 'k' in s
print 'k' in t
print 'c' not in t

for i in s:
    print i

s.add('z')
print s
s.update('pypi')
print s
s.remove('z')
print s
s -= set('pypi')
print s

del s
