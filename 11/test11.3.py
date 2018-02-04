#!/usr/bin/env python

"""Test demo 11.3 for chapter 11."""

from operator import add, mul
from functools import partial

add1 = partial(add, 1)
mul100 = partial(mul, 100)

print add1(10)
print mul100(5)
print ""

base_two = partial(int, base=2)
base_two.__doc__ = 'Convert base 2 string to int'
print base_two('10010')
print base_two.__doc__
