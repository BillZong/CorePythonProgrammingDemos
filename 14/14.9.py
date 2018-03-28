#!/usr/bin/env python
# encoding: UTF-8

"""Exercise answer 14.9 for chapter 14."""

import os

while True:
    cmd = raw_input('#: ')
    if cmd == 'exit':
        break
    else:
        output = os.popen(cmd).readlines()
        for out in output:
            print out,
