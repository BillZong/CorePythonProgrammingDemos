#!/usr/bin/env python
# encoding: UTF-8

"""Test demo 17.1 for chapter 17."""

# 测试ftp流程

from ftplib import FTP
import socket

# f = FTP('ftp.python.org')
# f.login('anoymous', '-help@python.org')
# f.dir()

try:
    f = FTP('python.org')
    f.login('anoymous', '-help@python.org')
    f.dir()
except (socket.error, socket.gaierror), (e, ge):
    print('登录失败: {0} {1}'.format(e, ge))
