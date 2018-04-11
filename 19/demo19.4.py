#!/usr/bin/env python
# encoding: UTF-8

"""Demo 19.4 for chapter 19."""

# 标签，按钮和进度条组件演示(tkhello4.py)
# 我们最后一个组件例子介绍了进度条组件，重点放在组件间通过回调函数的交互
# [诸如 resize()]。您对进度条组件的动作将影响标签组件上的文字。

from Tkinter import *


def resize(ev=None):
    """Resize label's font size."""
    label.config(font='Helvetica -%d bold' %
                 scale.get())

top = Tk()
top.geometry('400x300')

label = Label(top, text='Hello World!', font='Helvetica -12 bold')
label.pack(fill=Y, expand=1)

scale = Scale(top, from_=10, to=40, orient=HORIZONTAL, command=resize)
scale.set(12)
scale.pack(fill=X, expand=1)

quit = Button(top, text='QUIT', command=top.quit, activeforeground='white',
              activebackground='red')
quit.pack()

mainloop()
