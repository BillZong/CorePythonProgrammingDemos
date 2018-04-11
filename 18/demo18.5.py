#!/usr/bin/env python
# encoding: UTF-8

"""Demo 18.5 for chapter 18."""

# 使用可调用的类 (mtsleep4.py)
# 此例中，我们传了一个可调用的类(的实例)，而不是仅传一个函数。
# 相对 mtsleep3.py 中的方 法来说，这样做更具面向对象的概念。

import threading
from time import sleep, ctime

loops = [4, 2]


class ThreadFunc(object):
    """Docstring for ThreadFunc."""

    def __init__(self, func, args, name=''):
        """Init."""
        super(ThreadFunc, self).__init__()
        self.name = name
        self.func = func
        self.args = args

    def __call__(self):
        """Callable function will be called when start()."""
        # apply(self.func, self.args)
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
        t = threading.Thread(target=ThreadFunc(
            loop, (i, loops[i]), loop.__name__))
        threads.append(t)

    for i in nloops:
        threads[i].start()

    for i in nloops:
        threads[i].join()

    print 'all DONE at:', ctime()

if __name__ == '__main__':
    main()
