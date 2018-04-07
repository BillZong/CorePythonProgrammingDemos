#!/usr/bin/env python
# encoding: UTF-8

"""Exercise answer 16.6 for chapter 16."""

from socket import *

port = getservbyname("daytime", "udp")
addr = ("127.0.0.1", port)
# addr = ("ntp.sjtu.edu.cn", port)
conn = socket(AF_INET, SOCK_DGRAM)
conn.sendto("something", addr)
data, addr = conn.recvfrom(1024)
if data:
    print data
conn.close()
