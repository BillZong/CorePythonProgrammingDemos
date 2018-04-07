#!/usr/bin/env python
# encoding: UTF-8

"""Test demo 16.4 for chapter 16."""

from socket import *

print gethostbyname('www.baidu.com')
print gethostbyname_ex('www.baidu.com')
print ''

try:
    print gethostbyaddr('8.8.8.8')
    print gethostbyaddr('14.215.177.39')
except herror:
    print '解析IP失败'
print ''

print inet_aton('14.215.177.39')
print inet_pton(AF_INET, '14.215.177.39')

