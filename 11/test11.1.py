#!/usr/bin/env python

"""Demo 11.1 for chapter 11."""


def new_foo(arg1, arg2, *nkw, **kw):
    """Display regular args and all variable args."""
    print 'arg1 is:', arg1
    print 'arg2 is:', arg2
    for each_nkw in nkw:
        print 'additional non-keyword arg:', each_nkw
    for each_kw in kw.keys():
        print "additional keyword arg '%s': %s" % \
              (each_kw, kw[each_kw])

print(new_foo('wolf', 3, 'projects', freud=90, gamble=96))
