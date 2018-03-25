#!/usr/bin/env python
# encoding: UTF-8

"""Exercise 13.2 for chapter 13."""

from datetime import datetime
import shelve
import os

u"""用户注册。建立一个用户数据库(包括登录名、 密码和上次登录时间戳)类(参考练习 7-5
和 9-12)，来管理一个系统，该系统要求用户在登录后才能访问某些资源。这个数据库类对用
户进行管理，并在实例化操作时加载之前保存的用户信息，提供访问函数来添加或更新数据库
的信息。数据修改后，数据库会在垃圾回收时将新信息保存到磁盘。(参见__del__())."""

u"""''解析：
   1，建立一个类，包括 登陆名， 密码，时间戳， 而且需要读取：
       用到“序列化”对象的相关模块，数据结构用{"username": {"password", "datetime"}}.
   2, 登陆后才能访问：
        这里需要，给登陆状态做个标记：flag = False or True.
   3, 实例化操作时加载用户信息：
        需要在__init__构造器中，读取数据：shelve.open("filename", ......)
   4, 提供访问函数添加、更新数据库：
         这里要定义：deluser()、updateuser()等函数。
   5， 数据修改后，数据库会在垃圾回收是将“ 新信息”，保存到磁盘：
         这里用到__del__解构器, 结构器 是在引用计数为0时的前一刻，调用__del__
         结构器，这种特性可以定义__del__(), 来保存数据。"""


class UserDatabase(object):
    """docstring for UserDatabase."""

    def __init__(self, dbfile):
        """init."""
        self.db = {}
        if os.path.exists(dbfile):
            self.db = shelve.open(dbfile)
        self.dbfile = dbfile
        self.flag = False

    def __del__(self):
        """del."""
        data = shelve.open(self.dbfile)
        data.update(self.db)
        data.close()

    def register(self, user, pwd):
        """register."""
        if user in self.db:
            print 'User already register.'
            return
        self.flag = True  # 注册时默认其登录状态
        self.updateuser(user, pwd)

    def login(self, user, pwd):
        """login."""
        if user not in self.db:
            self.flag = False
        elif self.db[user]['password'] == pwd:
            self.db[user]['datetime'] = datetime.now()
            self.flag = True

    def deluser(self, user):
        """Delete user."""
        if self.flag:
            self.db.pop(user)
        else:
            print('Login first.')

    def updateuser(self, user, pwd):
        """Update user."""
        if self.flag:
            self.db[user] = {'password': pwd, 'datetime': datetime.now()}
        else:
            print('Login first.')
