#!/usr/bin/env python
# encoding: UTF-8

"""Exercise answer 16.8.1 for chapter 16."""

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


class ServerApp(App):
    def __init__(self, host, port):
        App.__init__(self)
        self.server = socket(AF_INET, SOCK_STREAM)
        self.server.setblocking(False)
        self.server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.server.bind((host, port))
        self.server.listen(1)
        self.inputs = [self.server]
        t = Thread(target=self.server_loop)
        t.setDaemon(True)
        t.start()

    def __del__(self):
        self.conn.close()

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
                        self.txt.insert(END, '[%s] stranger:' % ctime())
                        self.txt.insert(END, data)
                    else:
                        self.inputs.remove(reader)


if __name__ == '__main__':
    app = ServerApp('', 50007)
    app.mainloop()
