#!/usr/bin/env python

"""File filtering, ignore comment lines."""


def show_all_lines(file_path):
    """Show out all lines of a file, ignore comment lines."""
    try:
        f = open(file_path)
    except IOError:
        return None

    for line in f.readlines():
        strip_line = line.lstrip()
        if strip_line[0] == '#':
            continue
        elif '#' in strip_line:
            loc = strip_line.find('#')
            print strip_line[0:loc]
        else:
            print strip_line
