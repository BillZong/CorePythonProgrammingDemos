#!/usr/bin/env python
# encoding: UTF-8

"""Demo 14.1 for chapter 14."""

# loopmake.py, 一个简单地, 迅速生成和执行循环的计算机辅助软件工程(CASE)
# 更完整的版本应该包括: 用于字符串输入的不必要的引号, 输入数据的默认值,
#                    检测无效的返回和标识符; 不允许以关键字和内建名字作为变量名字

dashes = '\n' + '-' * 50
exec_dict = {
    'f': """# for loop
for %s in %s:
    print %s
""",
    's': """# sequence while loop
%s = 0
%s = %s
while %s < len(%s):
    print %s[%s]
    %s = %s + 1
""",
    'n': """# counting while loop
%s = %d
while %s < %d:
    print %s
    %s = %s + %d
"""
}


def main():
    ltype = raw_input('Loop type? (For/While) ')
    dtype = raw_input('Data type? (Number/Seq) ')

    if dtype == 'n':
        start = input('Starting value? ')
        stop = input('Ending value (non-inclusive)? ')
        step = input('Stepping value? ')
        seq = str(range(start, stop, step))
    else:
        seq = raw_input('Enter sequence: ')

    var = raw_input('Iterative variable name? ')

    if ltype == 'f':
        exec_str = exec_dict['f'] % (var, seq, var)
    elif ltype == 'w':
        if dtype == 's':
            svar = raw_input('Enter sequence name? ')
            exec_str = exec_dict['s'] % \
                (var, svar, seq, var, svar, svar, var, var, var)
        elif dtype == 'n':
            exec_str = exec_dict['n'] % \
                (var, start, var, stop, var, var, var, step)

    print dashes
    print 'your custom-generated code:' + dashes
    print exec_str + dashes
    print 'Test execution of the code:' + dashes
    exec exec_str
    print dashes


if __name__ == '__main__':
    main()
