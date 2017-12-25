#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""Test demo 8.4 for chapter 8."""

f = open('hhga.txt', 'r')
# 优化后的方案. 避免创建庞大的列表, 仅使用生成器表达式就完成了此次优化
print sum(len(word) for line in f for word in line.split())
f.close()
print ""


rows = [1, 2, 3, 17]


def cols():
    """Example of a simple generator."""
    yield 56
    yield 2
    yield 1

x_product_pairs = ((i, j) for i in rows for j in cols())
for pair in x_product_pairs:
    print pair
print ""


# # Version 0.1
# def get_longest_length_of_line(file_a):
#     """Get the longest line length of a file, without white spaces."""
#     f = open(file_a, 'r')
#     longest = 0
#     all_lines = f.readlines()
#     f.close()
#     for line in all_lines:
#         line_len = len(line.strip())
#         if line_len > longest:
#             longest = line_len
#     return longest

# # Version 0.2
# def get_longest_length_of_line(file_a):
#     """Get the longest line length of a file, without white spaces."""
#     f = open(file_a, 'r')
#     longest = 0
#     all_lines = [x.strip() for x in f.readlines()]
#     f.close()
#     for line in all_lines:
#         line_len = len(line)
#         if line_len > longest:
#             longest = line_len
#     return longest

# # Version 0.3
# def get_longest_length_of_line(file_a):
#     """Get the longest line length of a file, without white spaces."""
#     f = open(file_a, 'r')
#     all_line_lens = [len(x.strip()) for x in f]
#     f.close()
#     return max(all_line_lens)

# # Version 0.4
# def get_longest_length_of_line(file_a):
#     """Get the longest line length of a file, without white spaces."""
#     f = open(file_a, 'r')
#     longest = max(len(x.strip()) for x in f)
#     f.close()
#     return longest

# Version 0.5
def get_longest_length_of_line(file_a):
    """Get the longest line length of a file, without white spaces."""
    return max(len(x.strip()) for x in open(file_a))

print get_longest_length_of_line('/etc/bashrc')
