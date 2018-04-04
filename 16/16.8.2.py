#!/usr/bin/env python
# encoding: UTF-8

"""Exercise answer 16.8.2 for chapter 16."""

__author__ = 'Ibuki Suika'

from Tkinter import *
from ttk import *
from socket import *
from select import select
from threading import Thread
from time import ctime


class App(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.master.title('Python版聊天程式')
        self.frm1 = Frame()
        self.frm1.pack(fill=BOTH)
        self.frm2 = Frame()
        self.frm2.pack(side=BOTTOM, fill=X)
        self.txt = Listbox(self.frm1, width=100, height=20)
        self.txt.pack(side=LEFT, fill=X)
        self.bar = Scrollbar(self.frm1)
        self.bar.pack(side=RIGHT, fill=Y)
        self.txt['yscrollcommand'] = self.bar.set
        self.bar['command'] = self.txt.yview
        self. lbl = Label(self.frm2, text='待发送：')
        self.lbl.pack(side=LEFT)
        self.content = StringVar()
        self.entry = Entry(self.frm2, width=80, textvariable=self.content)
        self.entry.pack(side=LEFT)
        self.btn = Button(self.frm2, text='发送', command=self.send_msg)
        self.btn.pack(side=LEFT)

    def send_msg(self):
        pass


class ClientApp(App):
    def __init__(self, host, port):
        App.__init__(self)
        self.conn = socket(AF_INET, SOCK_STREAM)
        try:
            self.conn.connect((host, port))
            self.conn.setblocking(False)
        except error:
            self.txt.insert(END, '连接服务器失败')
        else:
            t = Thread(target=self.recv_msg_loop)
            t.setDaemon(True)
            t.start()

    def __del__(self):
        self.conn.close()

    def send_msg(self):
        s = self.content.get()
        self.txt.insert(END, '[%s] me:' % ctime())
        self.txt.insert(END, s)
        self.content.set('')
        self.conn.send(s)

    def recv_msg_loop(self):
        while True:
            readers, writers, exceptions = select([self.conn], [], [])
            if len(readers) > 0:
                s = self.conn.recv(1024)
                if s:
                    self.txt.insert(END, '[%s] stranger:' % ctime())
                    self.txt.insert(END, s)
                else:
                    break


if __name__ == '__main__':
    app = ClientApp('127.0.0.1', 50007)
    app.mainloop()
