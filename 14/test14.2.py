#!/usr/bin/env python
# encoding: UTF-8

"""Test demo 14.2 for chapter 14."""

import os

result = os.system('cat /etc/motd')
print result
print ''

os.system('uname -a')
print ''

f = os.popen('uname -a')
data = f.readline()
f.close()
print data

ret = os.fork()
if ret == 0:  # child code
    os.execvp('xbill', ['xbill'])
else:  # parent code
    print 'child process pid:', ret
    os.wait()
