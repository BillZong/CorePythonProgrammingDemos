#!/usr/bin/env python

"""Demo 12.5 for chapter 12."""

from __future__ import absolute_import
import sys
from sys import modules


print "sys module is reload()."
reload(sys)

print(sys.modules.keys())
print ''
print(modules.keys())
