#!/usr/bin/env python

"""Demo 6.1 for chapter 6."""

import string

# s = 'abcde'
# for i in [None] + range(-1, -len(s), -1):
#     print s[:i]
# print ""

# for i in range(-len(s), 0, 1):
#     print s[i:]
#     # print "i =", i, ",value =", s[i:]
# print ""

# s = s[::-1]
# for i in range(0, len(s), 1):
#     print s[i:]
# print ""

# print 'a' in s
# print 'f' not in s
# print ""

alphas = string.letters + '_'
nums = string.digits

print 'Welcome to the Identifier Checker v1.0'
print 'Testees must be at least 2 chars long.'
myInput = raw_input('Identifier to test?\n')

if len(myInput) > 1:
    if myInput[0] not in alphas:
        print '''invalid: first simbol must be
        alphabetic'''
    else:
        alphanumerics = alphas + nums
        for otherChar in myInput[1:]:
            if otherChar not in alphanumerics:
                print '''invalid: remaining
                symobols must be alphanumeric'''
                break
        else:
            print "okay as an identifier"
