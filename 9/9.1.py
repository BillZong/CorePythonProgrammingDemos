#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""File filtering, ignore comment lines."""

import re


def show_all_lines(file_path):
    """Show out all lines of a file, ignore comment lines."""
    def str_without_comment_in_line(str_line):
        stip_line = str_line.strip()
        if stip_line == '':
            return '\n'
        elif stip_line == '\n':
            return stip_line
        # 是否是可以忽略的行
        # 可忽略行的正则表达式列表
        reg = "[^\'\"]*.*#.*[^\'\"]*"
        z = re.compile(reg)
        match = re.search(z, str_line)
        if match:
            m = re.match(z, str_line)
            return m.group(0) + '\n'
        else:
            return str_line
#         regular_expressions = ["""\'.*#.*\'""", """\".*#.*\"
# """, """\'\'\'.*#.*\'\'\'""", """\"\"\".*#.*\"\"\""""]
#         for one in regular_expressions:
#             # try:
#             zz = re.compile(one)
#             # except re.SyntaxError(" error"):
#             if re.search(zz, str_line) is None:
#                 continue
#             else:
#                 return True  # 有匹配 则忽略
#         return False

    try:
        f = open(file_path)
    except IOError:
        return None

    for line in f.readlines():
        # print line.strip() + '\n',
        print str_without_comment_in_line(line),
        # index = line.find('#')  # 获取带注释句'#'的位置索引
        # if index == -1 or is_pass_line(line):
        #     if line.strip() != '':  # 排除纯空的行
        #         print line,
        # elif index != 0:
        #     if line.strip() != '':  # 排除纯空的行
        #         print line[:index] + '\n'

show_all_lines('9.1.py')
