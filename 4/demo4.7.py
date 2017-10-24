#!/usr/bin/env python

"""Test standard built in function."""

x = "python"
print id(x)

x = "Python"
print id(x)

i = 1
print id(i)

i += 1
print id(i)

i = i + 1
print id(i)

aList = [1, "2", -345]
print id(aList)

aList[1] = "100"
print id(aList)
