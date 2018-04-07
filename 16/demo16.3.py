#!/usr/bin/env python
# encoding: UTF-8

"""Demo 16.3 for chapter 16."""

# UDP 时间戳服务器 (tsUserv.py)
# 创建一个能接收客户的消息，在消息前加一个时间戳后返回的 UDP 服务器。

from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST, PORT)

udpSerSock = socket(AF_INET, SOCK_DGRAM)
udpSerSock.bind(ADDR)

while True:
    print 'waiting for message...'
    data, addr = udpSerSock.recvfrom(BUFSIZE)
    udpSerSock.sendto('[%s] %s' % (ctime(), data), addr)
    print '...received from and return to:', addr

udpSerSock.close()
