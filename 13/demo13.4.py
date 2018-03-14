#!/usr/bin/env python
# encoding: UTF-8

"""Demo 13.4 for chapter 13."""

from random import choice


class RandSeq(object):
    """Docstring for RandSeq."""
    def __init__(self, seq):
        """Constructor."""
        self.data = seq

    def __iter__(self):
        """Iterations."""
        return self

    def next(self):
        """Next iterator."""
        return choice(self.data)


if __name__ == '__main__':
    for eachItem in RandSeq(
        ('rock', 'paper', 'sissors')):
        print eachItem
