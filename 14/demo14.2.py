#!/usr/bin/env python
# encoding: UTF-8

"""Demo 14.2 for chapter 14."""

# 假设你是一位负责质量控制的软件开发者，你鼓励你的工程师将回归测试或
# 回归指令代码放到主代码中，但又不想让测试代码混合到产品代码中。
# 你可以让工程师创建字符串 形式的测试代码。当你的测试框架执行的时候，
# 它会检测函数是否定义了测试体，如果是的话，(求值并)执行它。如果不是，
# 便跳过，像通常一样执行。


def foo():
    return False


def bar():
    """bar() does not do much."""
    return True


foo.__doc__ = 'foo() does not do much'
# 后续添加的测试代码, 可用于独立的测试套件中!
foo.tester = '''
if foo():
    print 'PASSED'
else:
    print 'FAILED'
'''

for eachAttr in dir():
    obj = eval(eachAttr)
    if isinstance(obj, type(foo)):
        if hasattr(obj, '__doc__'):
            print '\nFunction "%s" has a doc string:\n\t%s' \
                % (eachAttr, obj.__doc__)
        if hasattr(obj, 'tester'):
            print 'Function "%s" has a tester... executing' % eachAttr
            exec obj.tester
        else:
            print 'Function "%s" has no tester... skipping' % eachAttr
    else:
        print '"%s" is not a function' % eachAttr
