#!/usr/bin/env python
# encoding: UTF-8

"""Demo 13.6 for chapter 13."""


class NumStr(object):
    """docstring for NumStr."""

    __typeErrorDesc = 'Illegal argument type for built-in operation'

    def __init__(self, num=0, string=''):
        """init."""
        super(NumStr, self).__init__()
        self.__num = num  # '隐藏'属性
        self.__string = string

    def __str__(self):
        """str()."""
        return '[%d :: %r]' %\
               (self.__num, self.__string)

    __repr__ = __str__

    def __add__(self, other):
        """add()."""
        if isinstance(other, self.__class__):
            return self.__class__(self.__num + other.__num,
                                  self.__string + other.__string)
        else:
            raise (TypeError, self.__class__.__typeErrorDesc)

    def __mul__(self, num):
        """mul()."""
        if isinstance(num, int):
            return self.__class__(self.__num * num, self.__string * num)
        else:
            raise (TypeError, self.__class__.__typeErrorDesc)

    def __nonzero__(self):
        """bool()."""
        return self.__num or len(self.__string)

    def __norm_cval(self, cmpres):
        """Compare cmpres with 0, only return -1, 0, and 1."""
        return cmp(cmpres, 0)

    def __cmp__(self, other):
        """cmp()."""
        return self.__norm_cval(cmp(self.__num, other.__num)
                                ) + self.__norm_cval(cmp(self.__string,
                                                         other.__string))

a = NumStr(3, 'foo')
b = NumStr(3, 'goo')
c = NumStr(2, 'foo')
d = NumStr()
e = NumStr(string='boo')
f = NumStr(1)
g = NumStr(3, 'coo')

print a
print b
print c
print d
print e
print f
print g
print ''

print a < b
print b < c
print a == a
print c == g
print ''

print b * 2
print b + e
print e + b
print ''

if d:
    print 'd not false'

if e:
    print 'e not false'
print ''

print cmp(a, b)
print cmp(a, c)
print cmp(c, g)
print ''
