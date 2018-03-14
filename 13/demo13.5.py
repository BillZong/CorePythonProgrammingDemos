#!/usr/bin/env python
# encoding: UTF-8

"""Demo 13.5 for chapter 13."""


class AnyIter(object):
    """docstring for AnyIter."""

    def __init__(self, data, safe=False):
        """Constructor."""
        super(AnyIter, self).__init__()
        self.safe = safe
        self.iter = iter(data)

    def __iter__(self):
        """iter."""
        return self

    def next(self, howmany=1):
        """Next function with specified number data."""
        retval = []
        for eachItem in range(howmany):
            try:
                retval.append(self.iter.next())
            except StopIteration as e:
                if self.safe:
                    break
                else:
                    raise e

        return retval

a = AnyIter(range(10), True)
i = iter(a)
for j in range(1, 6):
    print j, ':', i.next(j)
