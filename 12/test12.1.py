#!/usr/bin/env python

"""Demo 12.1 for chapter 12."""


def foo1():
    # """Testing of local namespace cover global space."""
    print '\ncalling foo()...'
    bar = 200
    print 'in foo(), bar is', bar

foo1.__doc__ = "Testing of local namespace cover global space."
foo1.version = 0.1


bar = 100
print 'in __main__, bar is', bar
foo1()
print ''
print foo1.__doc__
