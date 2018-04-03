#!/usr/bin/env python
# encoding: UTF-8

"""Demo 16.6 for chapter 16."""

# SocketServer 时间戳 TCP 客户端(tsTclntSS.py)
# 这是一个时间戳 TCP 客户端，它知道如何与 SocketServer 里 StreamRequestHandler 对象进行 通讯。

from socket import *

HOST = 'localhost'
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST, PORT)

while True:
    tcpCliSock = socket(AF_INET, SOCK_STREAM)
    tcpCliSock.connect(ADDR)
    data = raw_input('> ')
    if not data:
        break
    tcpCliSock.send('%s\n' % data)
    data = tcpCliSock.recv(BUFSIZE)
    if not data:
        break
    print data

tcpCliSock.close()
