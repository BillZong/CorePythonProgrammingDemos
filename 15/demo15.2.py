#!/usr/bin/env python
# encoding: UTF-8

"""Demo 15.2 for chapter 15."""

# gendata.py
# 为练习使用正则表达式生成随机数据，并将产生的数据输出到屏幕.

from random import randint, choice
from string import lowercase
from math import pow
# from sys import maxint
from time import ctime

doms = ('com', 'edu', 'net', 'org', 'gov')

myMax32Int = pow(2, 31)

for i in range(randint(5, 10)):
    # 64位int的数据太大, 导致无法生成时间
    # dtint = randint(0, maxint - 1)  # pick date
    dtint = randint(0, myMax32Int)  # pick date
    dtstr = ctime(dtint)

    shorter = randint(4, 7)  # login shorter
    em = ''
    for j in range(shorter):  # generate login
        em += choice(lowercase)

    longer = randint(shorter, 12)  # domain longer
    dn = ''
    for j in range(longer):  # create domain
        dn += choice(lowercase)

    print '%s::%s@%s.%s::%d-%d-%d' % (dtstr, em, dn, choice(doms),
                                      dtint, shorter, longer)
