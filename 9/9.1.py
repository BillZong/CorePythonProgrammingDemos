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
        index = line.find('#')  # 获取带注释句'#'的位置索引
        if index == -1 or is_pass_line(line):
            if line.strip() != '':  # 排除纯空的行
                print line,
        elif index != 0:
            if line.strip() != '':  # 排除纯空的行
                print line[:index] + '\n'

show_all_lines('9.1.py')
