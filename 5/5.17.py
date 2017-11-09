#!/usr/bin/env python

"""Random numbers of N."""

import random


def sorted_random_numbers():
    """Sorted the random numbers."""
    def n_number():
        """Creation of a number in [1, 100]."""
        return random.randrange(1, 100, 1)

    def random_numbers_of(n):
        """Creation of N random numbers."""
        random_list = []
        while n > 0:
            random_list.append(random.randrange(0, 230, 1))
            n -= 1
        return random_list

    # def cmp_value(x, y):
    #     """Comparation from smaller to larger."""
    #     if x > y:
    #         return 1
    #     elif x < y:
    #         return -1
    #     else:
    #         return 0

    random_list = random_numbers_of(n_number())
    random_list = sorted(random_list, cmp, lambda x: x)
    print "The sorted random numbers:"
    print random_list

sorted_random_numbers()
