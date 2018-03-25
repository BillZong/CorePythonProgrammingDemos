#!/usr/bin/env python
# encoding: UTF-8

"""Exercise 13.2 for chapter 13."""


class MoneyFmt(object):
    """docstring for MoneyFmt."""

    def __init__(self, value=0.0):
        """Constructor."""
        self.value = float(value)

    def update(self, value=None):
        u"""允许修改."""
        if value is not None:
            self.value = float(value)

    def __repr__(self):
        u"""显示为浮点数."""
        return repr(self.value)

    def __str__(self):
        u"""格式化显示."""
        is_neg = ""
        if self.value < 0:
            is_neg = "-"
        val = "%s￥%.2f" % (is_neg, self.value.__abs__())
        return val

    def __nonzero__(self):
        """Boolean test."""
        return not (self.value == 0.0)

cash = MoneyFmt(123.456)
print cash.__repr__
print cash
print ''

cash.update(10000.1234)
print cash.__repr__
print cash
print ''

cash.update(-0.3)
print cash.__repr__
print cash
print ''

cash.update(0)
print cash.__repr__
print cash
if not cash:
    print 'There is no money at all!'

