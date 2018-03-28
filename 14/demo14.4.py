#!/usr/bin/env python
# encoding: UTF-8

"""Demo 14.4 for chapter 14."""

import sys


def usage():
    """At least 2 arguments (incl. cmd name).
usage: demo14.4.py arg1 arg2 [arg3... ]"""
    print usage.__doc__
    sys.exit(-1)


argc = len(sys.argv)
if argc < 3:
    usage()

print "number of args enterd:", argc
print "args (incl. cmd name) were:", sys.argv
