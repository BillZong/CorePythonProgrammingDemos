#!/usr/bin/env python
# encoding: UTF-8

"""Demo 19.5 for chapter 19."""

# 运用 PFA 的路灯指示牌 GUI 程序(pfaGUI2.py)
# 按照指示类型创建适当前景、背景色的路灯指示牌。使用 PFA 帮助“模板化”常用 GUI 参数。

from functools import partial as pto
from Tkinter import Tk, Button, X
from tkMessageBox import showinfo, showwarning, showerror

WARN = 'warn'
CRIT = 'crit'
REGU = 'regu'

SIGNS = {
    'do not enter': CRIT,
    'railroad crossing': WARN,
    '55\nspeed limit': REGU,
    'wrong way': CRIT,
    'merging traffic': WARN,
    'one way': REGU,
}

critCB = lambda: showerror('Error', 'Error Button Pressed!')
