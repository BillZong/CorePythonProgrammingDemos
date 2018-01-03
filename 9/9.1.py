#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""File filtering, ignore comment lines."""

import re


def show_all_lines(file_path):
    """Show out all lines of a file, ignore comment lines."""
    def is_pass_line(str_line):
        # 是否是可以忽略的行
        # 可忽略行的正则表达式列表
        regular_expressions = ["""/'.*#.*/'""", """/\".*#.*/\"
""", """/'/'/'.*#.*/'/'/'""", """/\"/\"/\".*#.*/\"/\"/\""""]
        for one in regular_expressions:
            zz = re.compile(one)
            if re.search(zz, str_line) is None:
                continue
            else:
                return True  # 有匹配 则忽略
        return False

    try:
        f = open(file_path)
    except IOError:
        return None

    for line in f.readlines():
        if is_pass_line(line):
            continue

        elif '#' in line:
            strip_line = line.lstrip()
            if len(strip_line) == 0:
                print ''
                continue
            loc = strip_line.find('#')
            if loc == 1:
                print ''
                continue
            loc = line.find('#')
            print line[:loc],
            # This line won't be shown.
        else:
            print line,

show_all_lines('9.1.py')
