#!/usr/bin/env python

"""Demo 11.1 for chapter 11."""

from urllib import urlretrieve


def first_non_blank(lines):
    """Find first non blank line."""
    for each_line in lines:
        if not each_line.strip():
            continue
        else:
            return each_line


def first_last(webpage):
    """Find the first and last non blank line."""
    f = open(webpage)
    lines = f.readlines()
    print first_non_blank(lines),
    lines.reverse()
    print first_non_blank(lines),


def download(url='http://www.baidu.com', process=first_last):
    """Download of one page."""
    try:
        retval = urlretrieve(url)[0]
    except IOError:
        print "Read webpage(%s) failed" % (url)
        retval = None
    if retval:  # do some processing.
        process(retval)


if __name__ == '__main__':
    download()
