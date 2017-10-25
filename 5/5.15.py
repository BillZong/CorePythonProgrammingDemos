#!/usr/bin/env python

"""The greatest common devisor and the least common multiple."""


def gcd(x, y):
    """The greatest common devisor using euclid's algorithm."""
    while x % y != 0:
        x %= y
        (x, y) = (y, x)
    return y

print gcd(319, 377)
print gcd(98, 63)


def lcm(x, y):
    """The least common multiple."""
    return x * y / gcd(x, y)

print lcm(30, 45)
print lcm(15, 24)
