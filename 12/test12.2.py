#!/usr/bin/env python

"""Demo 12.2 for chapter 12."""

# import Tkinter as tk

# from Tkinter import Tk, Frame, Button, Entry, Canvas,\
#     Text, LEFT, DISABLED, NORMAL, RIDGE, END

# import sys
# print sys.path
# sys.path.append('/Users/billzong/repositories/\
# github/myself/CorePythonProgrammingDemos/12')
# print sys.path
# print ''

import importee


importee.show()
importee.foo = 123
print 'foo from importee:', importee.foo
importee.show()
