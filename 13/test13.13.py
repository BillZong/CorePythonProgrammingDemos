#!/usr/bin/env python
# encoding: UTF-8

"""Test demo 13.13 for chapter 13."""


class HideX(object):
    """docstring for HideX."""

    def __init__(self, x):
        """Init."""
        self.x = x

    @property
    def x(self):
        u"""文档是卸载getter里边的."""
        return ~self.__x

    @x.setter
    def x(self, in_x):
        assert isinstance(in_x, int), 'in_x must be an integer'
        self.__x = ~in_x


inst = HideX(10)
print 'inst.x =', inst.x
try:
    inst.x = 20
    print 'inst.x =', inst.x
    print HideX.x.__doc__
except AttributeError, e:
    print "Try to set {0} attribute \
{1} failed: {2}".format(inst, "x", e)
