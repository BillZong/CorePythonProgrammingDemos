#!/usr/bin/env python
# encoding: UTF-8

"""Test demo 16.2 for chapter 16."""

# 伪代码, tcp客户端流程

cs = socket() # 创建客户套接字
cs.connect() # 尝试连接服务器 # 通讯循环
comm_loop: # 通讯循环
    cs.send()/cs.recv() # 对话(发送/接收)
    cs.close() # 关闭客户套接字
