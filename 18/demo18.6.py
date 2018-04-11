#!/usr/bin/env python
# encoding: UTF-8

"""Demo 18.6 for chapter 18."""

# 子类化 Thread (mtsleep5.py)
# 我们现在要子类化 Thread 类，而不是创建它的实例。
# 这样做可以更灵活地定制我们的线程对象， 而且在创建线程的时候也更简单。

import threading
from time import sleep, ctime

loops = (4, 2)


class MyThread(threading.Thread):
    """Docstring for MyThread."""

    def __init__(self, func, args, name=''):
        """Init."""
        super(MyThread, self).__init__()
        self.func = func
        self.args = args
        self.name = name

    def run(self):
        """Will be called when start()."""
        self.func(*self.args)


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
        t = MyThread(loop, (i, loops[i]), loop.__name__)
        threads.append(t)

    for i in nloops:
        threads[i].start()

    for i in nloops:
        threads[i].join()

    print 'all DONE at:', ctime()

if __name__ == '__main__':
    main()
