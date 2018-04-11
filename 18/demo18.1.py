#!/usr/bin/env python
# encoding: UTF-8

"""Demo 18.1 for chapter 18."""

# 单线程中运行的循环 (onethr.py)
# 在单线程中顺序执行两个循环。一定要一个循环结束后，另一个才能开始。总时间是各个循环 运行时间之和。

from time import sleep, ctime


def loop0():
    """Loop 0."""
    print 'start loop 0 at:', ctime()
    sleep(4)
    print 'loop 0 done at:', ctime()


def loop1():
    """Loop 1."""
    print 'start loop 1 at:', ctime()
    sleep(2)
    print 'loop 1 done at:', ctime()


def main():
    """Main function."""
    print 'starting at;', ctime()
    loop0()
    loop1()
    print 'all DONE at:', ctime()

if __name__ == '__main__':
    main()
