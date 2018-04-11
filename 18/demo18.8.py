#!/usr/bin/env python
# encoding: UTF-8

"""Demo 18.8 for chapter 18."""

# 斐波那契，阶乘和累加和 (mtfacfib.py)
# 在这个多线程程序中，我们会分别在单线程和多线程环境中，运行三个递归函数。

from myThread import MyThread
from time import sleep, ctime


def fib(x):
    """Fibanacci function."""
    sleep(0.005)
    if x < 2:
        return 1
    return (fib(x - 2) + fib(x - 1))


def fac(x):
    """Factorial function."""
    sleep(0.1)
    if x < 2:
        return 1
    return (x * fac(x - 1))


def my_sum(x):
    """Sumary from 1 to x."""
    sleep(0.1)
    if x < 2:
        return 1
    return (x + my_sum(x - 1))

funcs = [fib, fac, my_sum]
n = 15


def main():
    """Main function."""
    nfuncs = range(len(funcs))

    print '*** Single thread.'
    for i in nfuncs:
        print 'starting', funcs[i].__name__, 'at:',\
              ctime()
        print funcs[i](n)
        print funcs[i].__name__, 'finished at"',\
                                 ctime()

    print '\n*** Multiple threads.'
    threads = []
    for i in nfuncs:
        t = MyThread(funcs[i], (n,), funcs[i].__name__)
        threads.append(t)

    for i in nfuncs:
        threads[i].start()

    for i in nfuncs:
        threads[i].join()
        print threads[i].get_result()

    print 'all DONE'

if __name__ == '__main__':
    main()
