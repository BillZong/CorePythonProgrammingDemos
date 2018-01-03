#!/usr/bin/env python

"""File accessing like head cmd."""


def head_of_file(file_name, lines=10):
    """File accessing like head cmd."""
    try:
        f = open(file_name, 'rU')
    except(IOError):
        print 'file(%s) not exist' % (file_name)

    for x in xrange(1, lines + 1):
        try:
            print f.readline(),
        except(EOFError):
            break
    f.close()

head_of_file('9.1.py', 8)
head_of_file('9.1.py', 100)
head_of_file('9_1.py', 10)
