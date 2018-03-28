#!/usr/bin/env python
# encoding: UTF-8

"""Test demo 14.1 for chapter 14."""


class C(object):
    """docstring for C."""

    def __call__(self, *args):
        u"""实现了该方法后, 意味着实例对象可被调用."""
        print "I'm callable! Called with args:\n", args

c = C()
print c

print callable(c)

c()
c(3)
c(3, 'no more, no less')
