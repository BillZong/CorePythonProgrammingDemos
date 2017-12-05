#!/usr/bin/env python

"""Exercise answer 8.1 for chapter 8."""


def if_state_pass(x):
    """Check the statement routine."""
    print 'A'
    if x > 0:
        print 'B'
        pass
    elif x < 0:
        print 'C'
        pass
    else:
        print 'D'
        pass
        print 'E'

if_state_pass(1)
print ''
if_state_pass(-1)
print ''
if_state_pass(0)
print ''
