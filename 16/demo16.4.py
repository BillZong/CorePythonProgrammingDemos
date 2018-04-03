#!/usr/bin/env python
# encoding: UTF-8

"""Demo 16.4 for chapter 16."""

# UDP 时间戳客户 (tsUclnt.py)
# 创建一个 UDP 客户端，程序会 示用户输入要传给服务器的信息，显示服务器返回的加了时间 戳的结果。

from socket import *

HOST = 'localhost'
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST, PORT)

udpCliSock = socket(AF_INET, SOCK_DGRAM)

while True:
    data = raw_input('> ')
    if not data:
        break
    udpCliSock.sendto(data, ADDR)
    data, ADDR = udpCliSock.recvfrom(BUFSIZE)
    if not data:
        break
    print data

udpCliSock.close()
