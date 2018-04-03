#!/usr/bin/env python
# encoding: UTF-8

"""Demo 16.2 for chapter 16."""

# TCP 时间戳客户端(tsTclnt.py)
# 创建一个 TCP 客户端，程序会 示用户输入要传给服务器的信息，显示服务器返回的加了 时间戳的结果

from socket import *

HOST = 'localhost'
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
    data = raw_input('> ')
    if not data:
        break
    tcpCliSock.send(data)
    data = tcpCliSock.recv(BUFSIZE)
    if not data:
        break
    print data

tcpCliSock.close()
