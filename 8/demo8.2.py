#!/usr/bin/env python

"""Demo 8.2 for chapter 8."""


def show_max_factor(num):
    """Show out a number's max factor."""
    count = num / 2
    while count > 1:
        if num % count == 0:
            print 'Largest factor of %d is %d' % \
                (num, count)
            break
        count -= 1
    else:
        print num, "is prime"

for eachNum in range(10, 21):
    show_max_factor(eachNum)
