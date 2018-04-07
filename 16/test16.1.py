#!/usr/bin/env python
# encoding: UTF-8

"""Test demo 16.1 for chapter 16."""

# 伪代码, tcp服务器流程

ss = socket()
ss.bind()
ss.listen()
inf_loop:
    cs = ss.accept() # 阻塞/非阻塞式连接
    comm_loop:
        cs.recv()/cs.send() # 对话(接收与发送)
        cs.close() # 关闭客户套接字

ss.close() # 关闭服务器套接字(可选)
