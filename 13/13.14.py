#!/usr/bin/env python
# encoding: UTF-8

"""Exercise 13.14 for chapter 13."""

import os
import platform


class Shell(object):
    u"""Shell class.

我们支持了多个指令, 包括ls, more, cat, cp, mv, rm, exit, help.
"""

    def __init__(self):
        """init."""
        self.unix_cmds = {'ls': 'ls',
                          'more': 'more',
                          'cat': 'cat',
                          'cp': 'cp',
                          'mv': 'mv',
                          'rm': 'rm'}
        self.windows_cmds = {'ls': 'dir',
                             'more': 'more',
                             'cat': 'type',
                             'cp': 'copy',
                             'mv': 'ren',
                             'rm': 'del'}
        self.is_windows = platform.system() == "Windows"

    def translate(self, cmd):
        """Translate unix cmd to dos cmd."""
        opt = cmd.split()
        if self.is_windows:
            if opt[0] in self.windows_cmds:
                opt[0] = self.windows_cmds[opt[0]]
        else:
            if opt[0] in self.unix_cmds:
                opt[0] = self.unix_cmds[opt[0]]

        return ' '.join(opt)

    def start(self):
        """Main function."""
        while 1:
            cmd = raw_input('#')
            cmd = self.translate(cmd)
            if cmd == 'exit':
                break
            elif cmd == 'help':
                print self.__class__.__doc__
            else:
                # 原博客用的os.popen函数，不是很理解
                os.system(cmd)

if __name__ == '__main__':
    s = Shell()
    s.start()
