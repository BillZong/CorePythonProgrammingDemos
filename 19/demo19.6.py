#!/usr/bin/env python
# encoding: UTF-8

"""Demo 19.6 for chapter 19."""

# GUI 文件遍历系统 (listdir.py)
# 这个稍高级一些的 GUI 程序扩大了组建的使用范围，演员名单里新增了列表框、
# 文本框、和滚 动条。而且还有大量的回调函数，例如鼠标点击、键盘输入、和滚动条操作。

import os
from time import sleep
from Tkinter import *


class DirList(object):
    """Docstring for DirList."""

    def __init__(self, initdir=None):
        """Init."""
        self.top = Tk()
        self.label = Label(self.top, text='Directory Lister v1.1')
        self.label.pack()

        # 提示框内容
        self.cwd = StringVar(self.top)

        # 标题
        self.dir1 = Label(self.top, fg='blue', font=('Helvetica', 12, 'bold'))
        self.dir1.pack()

        # 文件列表Frame
        self.dirfm = Frame(self.top)
        self.dirsb = Scrollbar(self.dirfm)
        self.dirsb.pack(side=RIGHT, fill=Y)
        # 滚动条被 Scrollbar.config()方法贴附在列表框上。
        self.dirs = Listbox(self.dirfm, height=15, width=50,
                            yscrollcommand=self.dirsb.set)
        # 列表框用 bind()方法把回调函数(setDirAndGo)和列表项绑定起来。
        # 绑定意味着把一个回调函数连接在键盘输入、鼠标动作、或其他什么事件上，
        # 当这个事件被用户触发时就会执行这个回调函数。
        # 当列表框中的任一项被双击时 setDirAndGo()函数就会被调用。
        self.dirs.bind('<Double-1>', self.set_dir_and_go)
        self.dirsb.config(command=self.dirs.yview)
        self.dirs.pack(side=LEFT, fill=BOTH)
        self.dirfm.pack()

        # 文件名信息/包括错误提示
        self.dirn = Entry(self.top, width=50, textvariable=self.cwd)
        # 在Mac上敲击键盘无效?
        self.dirn.bind('<Return>', self.do_ls)
        self.dirn.pack()

        # 按钮区域Frame
        self.bfm = Frame(self.top)
        self.clr = Button(self.bfm, text='Clear', command=self.clr_dir,
                          activeforeground='white', activebackground='green')
        self.ls = Button(self.bfm, text='List Directory', command=self.do_ls,
                         activebackground='green', activeforeground='white')
        self.quit = Button(self.bfm, text='Quit', command=self.top.quit,
                           activeforeground='white', activebackground='red')
        self.clr.pack(side=LEFT)
        self.ls.pack(side=LEFT)
        self.quit.pack(side=LEFT)
        self.bfm.pack()

        # 初始路径
        if initdir:
            self.cwd.set(os.curdir)
            self.do_ls()

    def show_error(self, err):
        """Show error."""
        self.cwd.set(err)
        self.top.update()
        sleep(2)
        if not (hasattr(self, 'last') and self.last):
            self.last = os.curdir
        self.cwd.set(self.last)
        self.dirs.config(selectbackground='LightSkyBlue')
        self.top.update()

    def clr_dir(self, ev=None):
        """Clear dir."""
        self.cwd.set('')

    def do_ls(self):
        """Do ls."""
        error = ''
        tdir = self.cwd.get()
        if not tdir:
            tdir = os.curdir

        if not os.path.exists(tdir):
            error = tdir + ': no such file'
        elif not os.path.isdir(tdir):
            error = tdir + ': not a directory'

        if error:
            self.show_error(error)
            return

        try:
            self.cwd.set('FETCHING DIRECTORY CONTENTS...')
            self.top.update()
            # 如果一切正确，它调用 os.listdir()来取得新的文件集合并替换列表框中的列表。
            dirlist = os.listdir(tdir)
            dirlist.sort()
            os.chdir(tdir)
            self.dir1.config(text=os.getcwd())
            self.dirs.delete(0, END)
            self.dirs.insert(END, os.curdir)
            self.dirs.insert(END, os.pardir)
            for eachFile in dirlist:
                self.dirs.insert(END, eachFile)
            self.cwd.set(os.curdir)
            self.dirs.config(selectbackground='LightSkyBlue')
        except Exception as e:
            self.show_error(e)
            return

    def set_dir_and_go(self, ev=None):
        """Set dir and go."""
        self.last = self.cwd.get()
        self.dirs.config(selectbackground='red')
        try:
            check = self.dirs.get(self.dirs.curselection())
        except Exception as e:
            self.show_error(e)
            return

        if not check:
            check = os.curdir
        self.cwd.set(check)
        self.do_ls()


def main():
    """Main function."""
    DirList(os.curdir)
    mainloop()

if __name__ == '__main__':
    main()
