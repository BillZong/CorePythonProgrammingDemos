#!/usr/bin/env python

"""Answer for 11.9 in chapter 11."""


def average(a_list):
    """Caculate the average of a list."""
    return reduce(lambda x, y: float(x) + float(y), a_list, 0) / len(a_list)

print average([1, 3, 5])
print average([1, '2', 5])
