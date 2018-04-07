#!/usr/bin/env python
# encoding: UTF-8

"""Demo 15.1 for chapter 15."""

# rewho.py 此脚本调用 who 命令，解析命令的输出结果，根据不同的空白符号分隔数据。

from os import popen
from re import split

f = popen('who', 'r')
for eachLine in f:
    print split('\s\s+|\t', eachLine.strip())
f.close()
