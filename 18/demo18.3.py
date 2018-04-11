#!/usr/bin/env python
# encoding: UTF-8

"""Demo 18.3 for chapter 18."""

# 使用线程和锁 (mtsleep2.py)
# 这里，使用锁比 mtsleep1.py 那里在主线程中使用 sleep()函数更合理。

import thread
from time import sleep, ctime

loops = [4, 2]


def loop(nloop, nsec, lock):
    """Loop function."""
    print 'start loop', nloop, 'at:', ctime()
    sleep(nsec)
    print 'loop', nloop, 'done at:', ctime()
    lock.release()


def main():
    """Main function."""
    print 'starting at:', ctime()
    locks = []
    nloops = range(len(loops))

    for i in nloops:
        lock = thread.allocate_lock()
        # 用这种方式获取锁
        lock.acquire()
        locks.append(lock)

    for i in nloops:
        thread.start_new_thread(loop, (i, loops[i], locks[i]))

    for i in nloops:
        while locks[i].locked():
            pass

    print 'all DONE at:', ctime()


if __name__ == '__main__':
    main()
