#!/usr/bin/env python
# encoding: UTF-8

"""Test demo 13.17 for chapter 13."""

from operator import *

vec1 = [12, 24]
vec2 = [2, 3, 4]
opvec = (add, sub, mul, div)  # using +, -, *, /
for eachOp in opvec:
    for i in vec1:
        for j in vec2:
            print '%s(%d, %d) = %d' % (eachOp.__name__, i, j, eachOp(i, j))
