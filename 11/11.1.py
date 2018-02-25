#!/usr/bin/env python

"""Answer for 11.1 in chapter 11."""


def count_to_four1():
    """Count to four version 1."""
    for eachNum in range(5):
        print eachNum,


def count_to_four2(n):
    """Count to four version 2."""
    for eachNum in range(n, 5):
        print eachNum,


def count_to_four3(n=1):
    """Count to four version 3."""
    for eachNum in range(n, 5):
        print eachNum,


# print count_to_four1(2)
# print count_to_four1(3)
# print count_to_four1(4)
# print count_to_four1(5)
print count_to_four1()
print ''

print count_to_four2(2)
print count_to_four2(3)
print count_to_four2(4)
print count_to_four2(5)
# print count_to_four2()
print ''

print count_to_four3(2)
print count_to_four3(3)
print count_to_four3(4)
print count_to_four3(5)
print count_to_four3()
print ''
