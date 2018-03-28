#!/usr/bin/env python
# encoding: UTF-8

"""Test demo 14.4 for chapter 14."""

import sys
import os
import atexit

# if hasattr(sys, 'exitfunc'):
#     prev_exit_func = sys.exitfunc
# else:
#     prev_exit_func = None

prev_exit_func = getattr(sys, 'exitfunc', None)


def my_exit_func(old_exit=prev_exit_func):
    # :
    # perform cleanup, the code is on you.
    # :
    print "%s 正在退出" % my_exit_func.__name__
    if old_exit is not None and callable(old_exit):
        old_exit()


sys.exitfunc = my_exit_func  # sys.exitfunc默认是不可用的, 替换成我们需要的方法


def my_at_exit():
    print u'我要退出进程了'


atexit.register(my_at_exit)

print os.environ
