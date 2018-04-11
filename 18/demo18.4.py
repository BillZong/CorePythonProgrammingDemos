#!/usr/bin/env python
# encoding: UTF-8

"""Demo 18.4 for chapter 18."""

# 使用 threading 模块 (mtsleep3.py)
# threading 模块的 Thread 类有一个 join()函数，允许主线程等待线程的结束。

import threading
from time import sleep, ctime

loops = [4, 2]


def loop(nloop, nsec):
    """Loop function."""
    print 'start loop', nloop, 'at:', ctime()
    sleep(nsec)
    print 'loop', nloop, 'done at:', ctime()


def main():
    """Main function."""
    print 'starting at:', ctime()
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        t = threading.Thread(target=loop, args=(i, loops[i]))
        threads.append(t)

    for i in nloops:
        threads[i].start()

    for i in nloops:
        threads[i].join()

    print 'all DONE at:', ctime()

if __name__ == '__main__':
    main()
