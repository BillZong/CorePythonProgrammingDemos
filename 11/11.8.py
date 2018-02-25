#!/usr/bin/env python

"""Answer for 11.8 in chapter 11."""

from random import randint


def leapyear(year):
    """Judge year is leap year or not."""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def filter_only_leapyear(a_list):
    """Filter out only leapyears."""
    return filter(leapyear, a_list)

years = []
for i in range(10):
    years.append(randint(0, 2018))

print years
print filter_only_leapyear(years)
print ''


years = [randint(0, 2018) for i in range(10)]
print years
print [n for n in years
       if (n % 4 == 0 and n % 100 != 0) or (n % 400 == 0)]
