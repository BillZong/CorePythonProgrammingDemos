#!/usr/bin/env python
# encoding: UTF-8

"""Test demo 13.5 for chapter 13."""


class C(object):
    """Nothing defined class."""

    pass

c = C()
print dir(c)
print c.__class__
print c.__dict__

c.foo = 1
c.bar = "SPAM"
print '%d can of %s please' % (c.foo, c.bar)
print c.__dict__
print ''

x = 3 + 0.14j
print dir(x)
print x.imag
print x.real
print x.conjugate()
print x.__float__
# Would crash
# print x.__dict__
