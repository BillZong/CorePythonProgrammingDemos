#!/usr/bin/env python
# encoding: UTF-8

"""Test demo 13.14 for chapter 13."""

import types


class C(object):
    """docstring for C."""

    pass


class CC:
    """docstring for CC."""

    pass

print type(C)
print type(CC)
print type(CC) is types.ClassType
