#!/usr/bin/env python
# encoding: UTF-8

"""Test demo 13.8 for chapter 13."""


class P(object):
    """Parent class."""

    def __init__(self):
        """Init."""
        print "calling P's constructor"

    def foo(self):
        """Printing."""
        print 'Hi, I am P-foo()'


class C(P):
    """Child class."""

    def __init__(self):
        """Init."""
        super(C, self).__init__()  # 调用基类的__init__()方法
        print "calling C's constructor"

    def foo(self):
        """Printing."""
        super(C, self).foo()  # 调用父类实例的方法
        print 'Hi, I am C-foo()'

c = C()
c.foo()
