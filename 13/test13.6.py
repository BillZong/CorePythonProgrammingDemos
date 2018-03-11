#!/usr/bin/env python
# encoding: UTF-8

"""Test demo 13.6 for chapter 13."""


class C(object):
    """Simple static member and instance property."""

    version = 1.2

c = C()
print C.version
print c.version
print ''

C.version += 0.1
print C.version
print c.version
print ''

c.version += 0.1  # "遮蔽"了类属性
print C.version
print c.version
print ''

print c.__dict__
print C.__dict__
print ''

del c.version  # 恢复了原来的类属性
print C.version
print c.version
print ''
print ''


class Foo(object):
    """Another simple static member and instance property."""

    x = {2017: 'poet1'}

foo = Foo()
print Foo.x
print foo.x
print ''

foo.x[2018] = "asdf"
print foo.x
print Foo.x
print ''

# 这个内容会导致崩溃
# del foo.x
