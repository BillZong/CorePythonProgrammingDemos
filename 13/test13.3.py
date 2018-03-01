#!/usr/bin/env python

"""Demo 13.3 for chapter 13."""


class P(object):
    """Class declaration."""

    def __init__(self):
        """Contructor."""
        print 'P is initialized.'

    def __del__(self):
        """Destructor."""
        print 'P is deleting.'
        del(self)  # call parent destrutor


class C(P):
    """Class declaration."""

    def __init__(self):
        """Contructor."""
        print 'C is initialized'

    def __del__(self):
        """Destructor."""
        print 'C is deleting.'
        P.__del__(self)  # call parent destrutor

c1 = C()
c2 = c1
c3 = c1
print id(c1), id(c2), id(c3)

del c1
del c2
del c3
