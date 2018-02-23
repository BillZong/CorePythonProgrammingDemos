#!/usr/bin/env python

"""Test demo 11.6 for chapter 11."""

x = 10


def foo():
    """Showing usage of simple lambda."""
    y = 5
    # bar = lambda: x + y  # E731 warning.
    # print bar()
    bar = lambda z: x + z  # E731 warning.
    print bar(y)
    y = 8
    print bar(y)

foo()
