#!/usr/bin/env python

"testing demo 3.2"

(x, y) = (1, "stupid")
print x
print y

(x, y) = (y, x)
print x
print y

print object.__doc__