#!/usr/bin/env python

"""Answer for 11.6 in chapter 11."""

import inspect


def current_frame():
    """Get the current frame info."""
    # callerframerecord = inspect.stack()[1]
    # frame = callerframerecord[0]
    # return inspect.getframeinfo(frame)
    return inspect.getframeinfo(inspect.stack()[1][0])


def printf(fmt, *args):
    """One implementation of C printf function."""
    print fmt % args

printf("(%s,%d): %s", current_frame().filename, current_frame().lineno,
       "Test printf function like C Language.")
