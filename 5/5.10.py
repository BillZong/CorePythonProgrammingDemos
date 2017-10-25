#!/usr/bin/env python

"""Hua shi to centus degree."""


def trans_f_to_c(f):
    """Transform f to c temperature."""
    return round((f - 32) * (5.0 / 9), 1)

print trans_f_to_c(105)
