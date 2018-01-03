#!/usr/bin/env python

"""Test demo 9.2 for chapter 9."""

import shelve

s = shelve.open("test.shdb", writeback=True)
s["a"] = "A very short sentence."
s.close()

s = shelve.open("test.shdb")
try:
    print s["a"]
    print s["A"]
except KeyError:
    pass

s.close()
