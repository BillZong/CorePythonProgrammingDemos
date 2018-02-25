#!/usr/bin/env python

"""Answer for 11.3 in chapter 11."""


def max2(a, b):
    """Copy function of max()."""
    if a >= b:
        return a
    else:
        return b


def min2(a, b):
    """Copy function of min()."""
    if a < b:
        return a
    else:
        return b


def my_max(*a_list):
    """Find out the maximun of a list."""
    if len(a_list) == 0:
        return None
    max_num = a_list[0]
    for eachNum in a_list[1:len(a_list)]:
        max_num = max2(max_num, eachNum)
    return max_num


def my_min(*a_list):
    """Find out the minimum of a list."""
    if len(a_list) == 0:
        return None
    min_num = a_list[0]
    for eachNum in a_list[1:len(a_list)]:
        min_num = min2(min_num, eachNum)
    return min_num


print my_max()
print my_max([])
print my_max(3, 6, 5, 12, 20)
print my_max([3, 6, 5, 12, 20])
print my_max([3, 6], ["1"])
print my_max(3, 6, 5, "12", 20)
print my_max(3, 6, 5, "12", [2, '25'], 20)
print ''

print my_min(3, 6, 5, 12, 20)
