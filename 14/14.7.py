#!/usr/bin/env python
# encoding: UTF-8

"""Exercise answer 14.7 for chapter 14."""

from subprocess import Popen, PIPE
# import os

dirOut = Popen('ls', stdout=PIPE, shell=True).stdout

filenames = dirOut.read()
print filenames

dirOut.close()

p = Popen('sort', stdin=PIPE, stdout=PIPE, shell=True)
p.stdin.write(filenames)
p.stdin.close()

print p.stdout.read()
p.stdout.close()
