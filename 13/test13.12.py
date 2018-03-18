#!/usr/bin/env python
# encoding: UTF-8

"""Test demo 13.12 for chapter 13."""


class ProtectAndHideX(object):
    """Docstring for ProtectAndHideX."""

    def __init__(self, x):
        """Init."""
        self.x = x

    def get_x(self):
        """Getter of x."""
        return ~self.__x

    def set_x(self, x):
        """Setter of x."""
        assert isinstance(x, int), 'x must be an integer'
        self.__x = ~x

    # 推荐使用, 因为有明确定义和控制属性访问. 类的名字空间也不会被弄乱了
    x = property(get_x, set_x, doc=r"测试用属性")

# inst = ProtectAndHideX('foo')  # assert failed!
inst = ProtectAndHideX(10)
print 'inst.x =', inst.x
try:
    inst.x = 20
    print 'inst.x =', inst.x
    print ProtectAndHideX.x.__doc__
except AttributeError, e:
    print "Try to set {0} attribute \
{1} failed: {2}".format(inst, "x", e)
