#!/usr/bin/env python
# encoding: UTF-8

"""Test demo 13.4 for chapter 13."""


class InstCt(object):
    """Class InstCt."""

    count = 0  # 一个类属性

    def __init__(self):
        """Init."""
        InstCt.count += 1

    def __del__(self):
        """Deinit."""
        InstCt.count -= 1

    def how_many(self):
        """Reference count."""
        return InstCt.count

a = InstCt()
b = InstCt()
print b.how_many()
print a.how_many()

del b
print a.how_many()

del a
print InstCt.count
