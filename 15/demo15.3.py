#!/usr/bin/env python
# encoding: UTF-8

"""Demo 15.3 for chapter 15."""

import re

data = 'Thu Feb 15 17:46:04 2007::uzifzf@dpyivihw.gov::1171590364-6-8'

# patt = '^(Mon|Tue|wed|Thu|Fri|Sat|Sun)'
patt = '^(\w){3}'
m = re.match(patt, data)
if m is not None:
    print m.group()
    print m.group(1)
print m.groups()
print ''


patt = '(\d+-\d+-\d+)'
print re.search(patt, data).group()

patt = '.+?(\d+-\d+-\d+)'
print re.match(patt, data).group(1)

patt = '-(\d+)-'
m = re.search(patt, data)
if m is not None:
    print m.group()
    print m.group(1)
print ''
