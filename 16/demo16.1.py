#!/usr/bin/env python
# encoding: UTF-8

"""Demo 16.1 for chapter 16."""

# TCP 时间戳服务器 (tsTserv.py), 创建一个能接收
# 客户的消息，在消息前加一个时间戳后返回的 TCP 服务器。

from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket()
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print 'waiting for connection...'
    tcpCliSock, addr = tcpSerSock.accept()
    print '...connected from:', addr

    while True:
        data = tcpCliSock.recv(BUFSIZE)
        if not data:
            break
        tcpCliSock.send('[%s] %s' % (ctime(), data))

    tcpCliSock.close()

tcpSerSock.close()
