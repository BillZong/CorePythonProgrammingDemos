#!/usr/bin/env python

"""Demo 6.1 for chapter 6."""

# from copy import copy, deepcopy
import copy

emptiestPossibleTupple = (None,)
print emptiestPossibleTupple

t = (1, 23, 'abc')
print 23 in t
print 'asdf' in t
print t[1:]
print ""

print str(t)
print len(t)
print max(t)
print min(t)
print cmp(t, (3, 234, "ecf"))
print ""

l = list(t)
print 'Remove element %s' % l.pop(1)
print tuple(l)
print ""

t = (['xyz', 123], 23, 0234)
print t[0][1]
print t
t[0][1] = ['sdf', 'r3i']
print "===>\n%s" % str(t)
print ""

print "t'ID = %d" % id(t)
swT = copy.copy(t)
print "swT'ID = %d" % id(swT)
deepT = copy.deepcopy(t)
print "deepT'ID = %d" % id(deepT)
