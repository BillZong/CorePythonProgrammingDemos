#!/usr/bin/env python

"""ID checker."""

import string
from keyword import kwlist

alphas = string.letters + '_'
nums = string.digits
alphaNums = alphas + nums

while True:
    print 'Welcome to the Identifier Checker v1.1'
    print 'Testees must be at least 1 char long.'
    myInput = raw_input('Identifier to test("quit" to quit)?\n')

    if len(myInput) > 0:
        if myInput == 'quit':
            break

        if myInput in kwlist:
            print """Invalid: you should not use keyword
'%s' as identifier""" % myInput
            continue

        if myInput[0] not in alphas:
            print "Invalid: first symbol must be alphabetic"
        else:
            ret = True
            for otherChar in myInput[1:]:
                if otherChar not in alphaNums:
                    ret = False
                    print "Invalid: remaining symbols must be alphanumeric"
                    break
            if ret:
                print "%s is a valid identifier." % myInput
    else:
        print 'You should input at least 1 char, please.\n'
