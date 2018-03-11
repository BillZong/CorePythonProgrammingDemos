#!/usr/bin/env python
# encoding: UTF-8

"""Test demo 13.10 for chapter 13."""


# MRO: Method Resolution Order. 文档解释顺序. Python 3后仅存在新式类,
# 目前MRO采用的C3算法, 而不是之前的BFS.
# class P1:  # 经典类, MRO使用深度优先算法. DFS
class P1(object):  # 新式类, MRO使用广度优先算法. BFS
    """Docstring for P1."""

    def foo(self):
        """Foo."""
        print 'called P1-foo()'


# class P2:
class P2(object):
    """Docstring for P2."""

    def foo(self):
        """Foo."""
        print 'called P2-foo()'

    def bar(self):
        """Bar."""
        print 'called P2-bar()'


class C1(P1, P2):
    """Docstring for C2."""

    pass


class C2(P1, P2):
    """Docstring for C2."""

    def bar(self):
        """Bar."""
        print 'called C2-bar()'


class GC(C1, C2):
    """Docstring for GC."""

    pass

gc = GC()
gc.foo()
gc.bar()
print GC.__mro__
print ''


class F(object):
    pass

class E(object):
    pass

class D(object):
    pass

class C(D, F):
    pass

class B(E, D):
    pass

class A(B, C):
    pass

print A.__mro__
