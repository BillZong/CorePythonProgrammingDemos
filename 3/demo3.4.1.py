#!/usr/bin/env python

"this is a test module"

import sys
import os

debug = True

class FooClass(object):
    """Foo Class"""
    pass

def test():
    "test function"
    foo = FooClass()
    if debug:
        print 'ran test()'
        print __doc__

if __name__ == '__main__':
    test()
