#!/usr/bin/env python

"""Test demo 8.1 for chapter 7."""

x, y = 4, 3
smaller = x if x < y else y
print smaller
print ''

names = 'Names'

for eachLetter in names:
    print 'Current letter:', eachLetter

for letterIndex in range(len(names)):
    print 'Letter:', names[letterIndex]

for index, letter in enumerate(names):
    print '%d, %s' % (index, letter)

print ''
