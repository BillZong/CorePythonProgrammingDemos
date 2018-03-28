#!/usr/bin/env python
# encoding: UTF-8

"""Test demo 14.3 for chapter 14."""

from subprocess import call, Popen, PIPE
import os

hosts = call(('cat', '/etc/hosts'))
print hosts
print ''


f = Popen(('uname', '-a'), stdout=PIPE).stdout
data = f.readline()
f.close()
print data,
print ''

f = Popen('who', stdout=PIPE).stdout
data = [eachLine.strip() for eachLine in f]
f.close()
for eachLine in data:
    print eachLine

os.sys.exit(1)
