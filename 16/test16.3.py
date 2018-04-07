#!/usr/bin/env python
# encoding: UTF-8

"""Test demo 16.3 for chapter 16."""

# 伪代码, UDP服务器

ss = socket()  # 创建一个服务器套接字
ss.bind()  # 绑定服务器套接字
inf_loop:
    cs = ss.recvfrom()/ss.sendto()  # 对话(接收与发送)
    ss.close()  # 关闭服务器套接字
