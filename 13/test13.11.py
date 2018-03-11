#!/usr/bin/env python
# encoding: UTF-8

"""Test demo 13.11 for chapter 13."""


class MyClass(object):
    """Docstring for MyClass."""

    def __init__(self):
        """Constructor."""
        super(MyClass, self).__init__()
        self.foo = 100

myInst = MyClass()
print hasattr(myInst, 'foo')
print getattr(myInst, 'foo')
print ''

print hasattr(myInst, 'bar')
try:
    print getattr(myInst, 'bar')
except Exception as e:
    print 'Get exception: %s' % e
    print getattr(myInst, 'bar', 'oops!')
print ''

setattr(myInst, 'bar', 'my attr')
print dir(myInst)
print ''

delattr(myInst, 'bar')
print dir(myInst)
print ''

print myInst.__dict__
print vars(myInst)
print ''

print locals()
print vars()
print ''
