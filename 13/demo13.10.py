#!/usr/bin/env python
# encoding: UTF-8

"""Demo 13.10 for chapter 13."""

from warnings import warn


class ReqStrSugRepr(type):
    """docstring for ReqStrSugRepr."""

    def __init__(cls, name, bases, attrd):
        """Constructor."""
        super(ReqStrSugRepr, cls).__init__(name, bases, attrd)

        if '__str__' not in attrd:
            raise TypeError("Class requires overriding of __str__()")

        if '__repr__' not in attrd:
            warn('Class suggests overriding of __repr__()\n', stacklevel=3)

print '*** Defined ReqStrSugRepr (meta)class\n'


class Foo(object):
    """docstring for Foo."""

    __metaclass__ = ReqStrSugRepr

    def __str__(self):
        """__str__."""
        return 'Instance of class:\
', self.__class__.__name__

    def __repr__(self):
        """__repr__."""
        return self.__class__.__name__

print '*** Defined Foo class\n'


class Bar(object):
    """docstring for Bar."""

    __metaclass__ = ReqStrSugRepr

    def __str__(self):
        """__str__."""
        return 'Instance of class:\
', self.__class__.__name__

print '*** Defined Bar class\n'


class FooBar(object):
    """docstring for FooBar."""

    __metaclass__ = ReqStrSugRepr

print '*** Defined FooBar class\n'
