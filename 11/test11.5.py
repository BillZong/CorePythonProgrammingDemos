#!/usr/bin/env python

"""Test demo 11.5 for chapter 11."""


def counter(start_at=0):
    """Counter closure for start_at num."""
    count = [start_at]

    def incr():
        """Increment for first list element."""
        count[0] += 1
        return count[0]

    return incr

count = counter(5)
print count()
print count()
print count()

count2 = counter(100)
print count2()
print count2()
print ""
