#!/usr/bin/env python
# encoding: UTF-8

"""Exercise answer 16.9.1 for chapter 16."""

__author__ = 'Ibuki Suika'

# 尚未完成

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
        self.master.title('多人聊天程序')
        self.frm1 = Frame()
        self.frm1.pack(fill=BOTH)
        self.frm2 = Frame()
        self.frm2.pack(side=BOTTOM, fill=X)
        self.frm3 = Frame()
        self.frm3.pack(side=BOTTOM, fill=X)
        self.txt = Listbox(self.frm1, width=105, height=20)
        self.txt.pack(side=LEFT, fill=X)
        self.bar = Scrollbar(self.frm1)
        self.bar.pack(side=RIGHT, fill=Y)
        self.txt['yscrollcommand'] = self.bar.set
        self.bar['command'] = self.txt.yview
        self. lbl = Label(self.frm2, text='待发送：')
        self.lbl.pack(side=LEFT)
        self.content = StringVar()
        self.entry = Entry(self.frm2, width=60, textvariable=self.content)
        self.entry.pack(side=LEFT)
        self.lbl_0 = Label(self.frm2, text='发送往：')
        self.lbl_0.pack(side=LEFT)
        self.cb_content = StringVar()
        self.cb_list = []
        self.cb = Combobox(self.frm2,  width=15, textvariable=self.cb_content, state='readonly', values=self.cb_list)
        self.cb.pack(side=LEFT)
        self.btn = Button(self.frm2, text='发送', command=self.send_msg)
        self.btn.pack(side=LEFT)
        self.lb1_1 = Label(self.frm3, text='IP地址：')
        self.lb1_1.pack(side=LEFT)
        self.ip_content = StringVar()
        self.ip_entry = Entry(self.frm3, width=60, textvariable=self.ip_content)
        self.ip_entry.pack(side=LEFT)
        self.lbl_2 = Label(self.frm3, text='端口号：')
        self.lbl_2.pack(side=LEFT)
        self.port_content = StringVar()
        self.port_entry = Entry(self.frm3, width=18, textvariable=self.port_content)
        self.port_entry.pack(side=LEFT)
        self.connect_btn = Button(self.frm3, text='连接', command=self.connect)
        self.connect_btn.pack(side=LEFT)

    def send_msg(self):
        pass

    def connect(self):
        pass


class ChatApp(App):
    def __init__(self):
        App.__init__(self)
        self.server = socket(AF_INET, SOCK_STREAM)
        self.server.setblocking(False)
        self.server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.server.bind(('', 50007))
        self.server.listen(100)
        self.inputs = [self.server]
        t = Thread(target=self.server_loop)
        t.setDaemon(True)
        t.start()

    def __del__(self):
        self.server.close()

    def send_msg(self):
        s = self.content.get()
        self.txt.insert(END, '[%s] me:' % ctime())
        self.txt.insert(END, s)
        self.content.set('')
        if len(self.inputs) == 2:
            self.inputs[1].send(s)

    def server_loop(self):
        while True:
            readers, writers, exceptions = select(self.inputs, [], [])
            for reader in readers:
                if reader is self.server:
                    conn, addr = reader.accept()
                    conn.setblocking(False)
                    self.inputs.append(conn)
                else:
                    data = reader.recv(1024)
                    if data:
                        addr = reader.getpeername()
                        self.txt.insert(END,  '[%s] (%s, %d)' % (ctime(), addr[0], addr[1]))
                        self.txt.insert(END, data)
                    else:
                        self.inputs.remove(reader)

    def connect(self):
        host = self.ip_content.get()
        port = int(self.port_content.get())
        print host, port
        conn = socket(AF_INET, SOCK_STREAM)
        conn.connect((host, port))
        conn.setblocking(False)
        self.inputs.append(conn)
        self.cb_list.append('%s:%d' % (host, port))
        self.cb['values'] = self.cb_list

if __name__ == '__main__':
    app = ChatApp()
    app.mainloop()
