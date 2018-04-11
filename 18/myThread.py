#!/usr/bin/env python
# encoding: UTF-8

"""Demo 18.7 for chapter 18."""

# MyThread 子类化 Thread (myThread.py)
# 为了让 mtsleep5.py 中，Thread 的子类更为通用，
# 我们把子类单独放在一个模块中，并加上一 个 getResult()函数用以返回函数的运行结果。

import threading
from time import ctime


class MyThread(threading.Thread):
    """Docstring for MyThread."""

    def __init__(self, func, args, name=''):
        """Init."""
        super(MyThread, self).__init__()
        self.func = func
        self.args = args
        self.name = name

    def get_result(self):
        """Get run result."""
        return self.res

    def run(self):
        """Called when start()."""
        print 'starting', self.name, 'at:', \
              ctime()
        self.res = self.func(*self.args)
        print self.name, 'finished at:', ctime()
