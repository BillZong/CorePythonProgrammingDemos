#!/usr/bin/env python
# encoding: UTF-8

"""Demo 19.2 for chapter 19."""

# 按钮组件演示(tkhello2.py)
# 本例和 tkhello1.py 完全相同，除了我们创建的是按钮组件而非标签组件。

import Tkinter

top = Tkinter.Tk()
quit = Tkinter.Button(top, text='Hello World', command=top.quit)
quit.pack()
Tkinter.mainloop()
