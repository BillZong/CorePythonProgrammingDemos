#!/usr/bin/env python
# encoding: UTF-8

"""Test demo 13.15 for chapter 13."""

from time import ctime

print '*** Welcome to Metaclasses!'
print '\tMetaclass declaration first.'


class MetaC(type):
    """docstring for MetaC."""

    def __init__(cls, name, bases, attrd):
        """Contructor."""
        super(MetaC, cls).__init__(name, bases, attrd)
        print '*** Created class %r at: %s' % (name, ctime())

print '\tClass "Foo declaration next.'


class Foo(object):
    """docstring for Foo."""

    __metaclass__ = MetaC

    def __init__(self):
        """Constructor."""
        print '*** Instantiated class %r at: %s' % (
            self.__class__.__name__, ctime())

print '\tClass "Foo" instantiation next.'

f = Foo()
print '\tDone.'
