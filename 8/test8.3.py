#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""Test demo 8.3 for chapter 8."""

# allURLs = ["http://abc.com", "ftp://test.cn"]
# for eachURL in allURLs:
#     if not eachURL.startsWith('http://'):
#         allURLs.remove(eachURL)

# RuntimeError: dictionary changed size during iteration
# myDict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# for eachKey in myDict:
#     print eachKey, myDict[eachKey]
#     del myDict[eachKey]

import os

print map(lambda x: x ** 2, range(6))
print [x ** 2 for x in range(6)]
print ""


seq = [11, 10, 9, 92, 4, 20, 31, 73, 8, 25, 96]
print filter(lambda x: x % 2, seq)
# 可以取代内建的map()函数以及lambda, 而且效率更高
print [x for x in seq if x % 2]
print ""


print [(x + 1, y + 1) for x in range(3) for y in range(5)]
print ""

f = open('hhga.txt', 'r')
print len([word for line in f for word in line.split()])
print os.stat('hhga.txt').st_size
print ""


f.seek(0)
# 文件很大的时候, 这个列表也会很长, 内存性能会很低.
print sum([len(word) for line in f for word in line.split()])
f.close()
