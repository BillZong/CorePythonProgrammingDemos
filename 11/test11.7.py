#!/usr/bin/env python

"""Test demo 11.7 for chapter 11."""


def factorial(n):
    """Factorial value for positive integer n."""
    if n == 0 or n == 1:  # 0! = 1, 1! = 1
        return 1
    else:
        return n * factorial(n - 1)

print factorial(5)
print factorial(20)
