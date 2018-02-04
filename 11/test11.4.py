#!/usr/bin/env python

"""Test demo 11.4 for chapter 11."""

from functools import partial
import Tkinter

root = Tkinter.Tk()
myBotton = partial(Tkinter.Button, root,
                   fg='white', bg='blue')
b1 = myBotton(text='Button 1')
b2 = myBotton(text='Button 2')
qb = myBotton(text='QUIT', bg='red',
              command=root.quit)
b1.pack()
b2.pack()
qb.pack(fill=Tkinter.X, expand=True)
root.title('PFAs!')
root.mainloop()
