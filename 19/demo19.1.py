#!/usr/bin/env python
# encoding: UTF-8

"""Demo 19.1 for chapter 19."""

# 标签组件演示(tkhello1.py)
# 我们的第一个 Tkinter 例子是......还能是什么呢?
# “Hello World!”具体地说，是介绍我们 的第一个组件:标签。

import Tkinter

top = Tkinter.Tk()
label = Tkinter.Label(top, text='Hello Wold')
label.pack()
Tkinter.mainloop()
