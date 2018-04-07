#!/usr/bin/env python
# encoding: UTF-8

"""Demo 16.5 for chapter 16."""

# SocketServer 时间戳服务器(tsTservSS.py)
# 使用 SocketServer 里的 TCPServer 和 StreamRequestHandler 类创建一个时间戳 TCP 服务器。

from SocketServer import (TCPServer as TCPS, StreamRequestHandler as SRH)
from time import ctime

HOST = ''
PORT = 21567
ADDR = (HOST, PORT)


class MyRequestHandler(SRH):
    def handle(self):
        print '...connected from:', self.client_address
        self.wfile.write('[%s] %s' % (ctime(), self.rfile.readline()))


tcpServ = TCPS(ADDR, MyRequestHandler)
print 'waiting for connection...'
tcpServ.serve_forever()
