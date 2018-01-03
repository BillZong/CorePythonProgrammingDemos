#!/usr/bin/env python

"""File lines counting function."""


def lines_of_file(file_name):
    """File lines counting function."""
    try:
        f = open(file_name)
    except(IOError):
        print 'file(%s) not exist' % (file_name)
        return

    all_lines = f.readlines()
    print 'Length of file(%s) is %d' % (file_name, len(all_lines))

lines_of_file('9.1.py')
lines_of_file('9.2.py')
lines_of_file('9_2.py')
