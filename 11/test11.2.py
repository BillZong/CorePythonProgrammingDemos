#!/usr/bin/env python

"""Demo 11.2 for chapter 11."""

from random import randint as ri

print [n for n in [ri(1, 99) for i in range(10)] if n % 2]
print ""

print map((lambda x: x + 2), range(6))
print [x + 2 for x in range(6)]
print map((lambda x: x ** 3), range(6))
print [x ** 3 for x in range(6)]
print ""

print map(lambda x, y: x + y, [1, 3, 5], [2, 4, 6])
print map(lambda x, y: (x + y, x - y), [1, 3, 5], [2, 4, 6])
print ""

print map(None, [1, 3, 5], [2, 4, 6])
print zip([1, 3, 5], [2, 4, 6])
print ""

print 'The total is:', reduce((lambda x, y: x + y), range(5))
