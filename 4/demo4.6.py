#!/usr/bin/env python

"""Standard __builtin__ function."""

import sys
# import types
from types import FloatType
from types import IntType
from types import LongType
from types import ComplexType
import math
from decimal import Decimal


print cmp(3, '2')
print repr(sys)
print str(sys)
print type(sys)
print type(type(sys))


class FooClass(object):
    """Docstring for FooClass."""

    def __init__(self):
        """Initialization."""
        super(FooClass, self).__init__()

c = FooClass()
exp = repr(c)
print exp
print isinstance(c, FooClass)

print type({})
print type(type)

# TODO: not working in python 2.7.10?
# print eval(exp).


def display_num_type(num):
    """Show number type."""
    print num, 'is',
    if isinstance(num, IntType):
        print 'an integer'
    elif isinstance(num, LongType):
        print 'an long'
    elif isinstance(num, FloatType):
        print 'a float'
    elif isinstance(num, ComplexType):
        print 'a complex'
    else:
        print 'not a number at all'

display_num_type(0)
display_num_type(0L)
display_num_type(0.0)
display_num_type(0 + 0j)
display_num_type("test")

print "the ** operator"
print -3 ** 2
print (-3) ** 2

print "the bit moving operator"
print -3 << 2
print (-3) << 2
# print 3.2 << 2 #ValueError

print "the opersite operator"
print ~(-3)

print "base value initialization"
print int("32")
print complex("3.2+2.9j")

print "abs()"
print abs(3.2 + 2.9j)

print "coerce()"
print coerce(1, 2)
print coerce(1.3, 134L)
print coerce(1j, 134L)
print coerce(1.23 - 41j, 134L)

print "divmod()"
print divmod(10, 3)
print divmod(3, 10)
print divmod(10, 2.5)
print divmod(2.5, 10)
print divmod(2 + 1j, 0.5 - 1j)
print ((2 + 1j) / (0.5 - 1j)).real

print "pow()"
print pow(2, 5)
print pow(5, 2)
print pow(3.1415926535458979, 2)
print pow(1 + 1j, 2)
print pow(1 + 1j, 3)
print pow(3, 5, 26)

print "round()"
print round(3)
print round(3.45)
print round(3.49999)
print round(3.49999, 1)
print "the value of pai:"
for eachNum in range(25):
    print round(math.pi, eachNum)

print "digital/hex/octoal number transform"
print hex(255)
print hex(324029898234)
print oct(255)
print oct(324029898234)

print "chr() & ord()"
print ord('a')
print chr(48)
print unichr(49399)

print "Decimal class"
dec = Decimal('.1')
print dec
# print dec + 0.1 //TypeError
print dec + Decimal('1.0')
