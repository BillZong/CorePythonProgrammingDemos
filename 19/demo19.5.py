#!/usr/bin/env python
# encoding: UTF-8

"""Demo 19.5 for chapter 19."""

# 运用 PFA 的路灯指示牌 GUI 程序(pfaGUI2.py)
# 按照指示类型创建适当前景、背景色的路灯指示牌。使用 PFA 帮助“模板化”常用 GUI 参数。

from functools import partial as pto
from Tkinter import Tk, Button, X
from tkMessageBox import showinfo, showwarning, showerror

WARN = 'Warn'
CRIT = 'Crit'
REGU = 'Regu'

SIGNS = {
    'do not enter': CRIT,
    'railroad crossing': WARN,
    '55\nspeed limit': REGU,
    'wrong way': CRIT,
    'merging traffic': WARN,
    'one way': REGU,
}

critCB = lambda: showerror('Error', 'Error Button Pressed!')
warnCB = lambda: showwarning('Warning', 'Warning Button Pressed!')
infoCB = lambda: showinfo('Info', 'Info Button Pressed!')

top = Tk()
top.title('Road Signs')

# bg在Mac上无效, 建议使用ttk替代Tkinter
Button(top, text='QUIT', command=top.quit,
       activebackground='red', activeforeground='white').pack()

MyButton = pto(Button, top)
CritButton = pto(MyButton, command=critCB,
                 activebackground='white', activeforeground='red')
WarnButton = pto(MyButton, command=warnCB, activebackground='goldenrod1')
ReguButton = pto(MyButton, command=infoCB, activebackground='white')

for eachSign in SIGNS:
    signType = SIGNS[eachSign]
    cmd = '%sButton(text=%r%s).pack(fill=X, expand=True)' %\
          (signType.title(), eachSign,
           '.upper()' if signType == CRIT else '.title()')
    eval(cmd)

top.mainloop()
