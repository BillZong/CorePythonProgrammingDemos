#!/usr/bin/env python
# encoding: UTF-8

"""Test demo 13.16 for chapter 13."""

from warnings import warn


class ReqStrSugRepr(type):
    """docstring for ReqStrSugRepr."""

    def __init__(cls, name, bases, attrd):
        """Constructor."""
        super(ReqStrSugRepr, cls).__init__(name, bases, attrd)

        if '__str__' not in attrd:
            raise TypeError("Class requires overriding of __str__()")

        if '__repr__' not in attrd:
            warn('Class suggests overriding of __repr__()\n', stacklevel=3)
