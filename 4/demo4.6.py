#!/usr/bin/env python

"""Number type distinguish."""

from types import IntType
from types import FloatType
from types import LongType
from types import ComplexType


def display_num_type(num):
    """Display number type name."""
    if isinstance(num, (IntType, FloatType, LongType, ComplexType)):
        print num, 'is a number'
    else:
        print num, 'is not a number!'

display_num_type(0)
display_num_type(0L)
display_num_type(0.0)
display_num_type(0 + 0j)
display_num_type('abc')
