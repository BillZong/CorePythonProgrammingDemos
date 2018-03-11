#!/usr/bin/env python
# encoding: UTF-8

"""Test demo 13.7 for chapter 13."""


class TestStaticMethod(object):
    """Testing static method."""

    @staticmethod
    def foo():
        """Nothing."""
        print 'calling static method foo()'


class TestClassMethod(object):
    """Testing class method."""

    @classmethod
    def foo(cls):
        """Nothing."""
        print 'calling class method foo()'
        print 'foo() is part of class:', cls.__name__

tsm = TestStaticMethod()
TestStaticMethod.foo()
tsm.foo()
print ''

tcm = TestClassMethod()
TestClassMethod.foo()
tcm.foo()
print ''

print TestClassMethod.__bases__
print ''
