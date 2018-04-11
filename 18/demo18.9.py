#!/usr/bin/env python
# encoding: UTF-8

"""Demo 18.9 for chapter 18."""

# 生产者-消费者问题 (prodcons.py)
# 这个实现中使用了 Queue 对象和随机地生产(和消耗)货物的方式。
# 生产者和消费者相互独立 并且并发地运行。

from random import randint
from time import sleep
from Queue import Queue
from myThread import MyThread


def write_q(queue):
    """Producer."""
    print 'producing object for Q...'
    queue.put('xxx', 1)
    print "size now", queue.qsize()


def read_q(queue):
    """Consumer."""
    queue.get(1)
    print 'consumed object from Q... size now',\
          queue.qsize()


def writer(queue, loops):
    """Writer."""
    for i in range(loops):
        write_q(queue)
        sleep(randint(1, 3))


def reader(queue, loops):
    """Reader."""
    for i in range(loops):
        read_q(queue)
        sleep(randint(2, 5))

funcs = [writer, reader]
nfuncs = range(len(funcs))


def main():
    """Main function."""
    nloops = randint(5, 8)
    q = Queue(32)

    threads = []
    for i in nfuncs:
        t = MyThread(funcs[i], (q, nloops), funcs[i].__name__)
        threads.append(t)

    for i in nfuncs:
        threads[i].start()

    for i in nfuncs:
        threads[i].join()

    print 'all DONE'

if __name__ == '__main__':
    main()
