#!/usr/bin/env python
# encoding: UTF-8

"""Demo 19.3 for chapter 19."""

# 标签和按钮组件演示(tkhello3.py)
# 本例同时展示了标签和按钮组件。既然我们已经了解了按钮组件和如何配置它，
# 我们就可以设 置的更多一些，而不必像以前那样大都使用缺省参数。

import Tkinter

top = Tkinter.Tk()

hello = Tkinter.Label(top, text='Hello')
hello.pack()

quit = Tkinter.Button(top, text='QUIT', command=top.quit,
                      bg='blue', fg='white')
# quit.pack()
quit.pack(fill=Tkinter.X, expand=1)

Tkinter.mainloop()
