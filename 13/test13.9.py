#!/usr/bin/env python
# encoding: UTF-8

"""Test demo 13.9 for chapter 13."""


class RoundFloat(float):
    """Rounded float class."""

    def __new__(cls, val):  # 修改创建的类方法
        """Modified constructor with round value."""
        # 类方法的super, 跟实例方法传入的对象不同!
        return super(RoundFloat, cls).__new__(cls, round(val, 2))

print RoundFloat(1.5955)
print RoundFloat(1.5945)
print RoundFloat(-1.5955)
print ''


class SortedKeyDict(dict):
    """New modified dictionary with sorted keys."""

    def keys(self):
        """Instance override method."""
        # return sorted(self.keys())  # 简单版本, 等效~
        return sorted(super(SortedKeyDict, self).keys())

d = SortedKeyDict((('zheng-cai', 67), ('hui-jun', 68), ('xin-yi', 2)))
print 'By iterator:'.ljust(12), [key for key in d]
print 'By keys()'.ljust(12), d.keys()
