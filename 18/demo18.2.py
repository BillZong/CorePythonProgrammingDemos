#!/usr/bin/env python
# encoding: UTF-8

"""Demo 18.2 for chapter 18."""

# 使用 thread 模块 (mtsleep1.py)
# 这儿执行的是和 onethr.py 中一样的循环，不同的是，
# 这一次我们使用的是 thread 模块提供的简单的多线程的机制。
# 两个循环并发地被执行(显然，短的那个先结束)。
# 总的运行时间为最慢的那 个线程的运行时间，而不是所有的线程的运行时间之和。

import thread
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
    thread.start_new_thread(loop0, ())
    thread.start_new_thread(loop1, ())
    sleep(6)
    print 'all DONE at:', ctime()

if __name__ == '__main__':
    main()
