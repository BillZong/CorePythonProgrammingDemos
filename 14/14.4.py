#!/usr/bin/env python
# encoding: UTF-8

"""Exercise answer 14.4 for chapter 14."""

# import os
# from subprocess import call
from commands import getoutput

if __name__ == '__main__':
    result = getoutput('ls')
    print result
    # res = os.system('ls')
    # res = call('ls', shell=False)
