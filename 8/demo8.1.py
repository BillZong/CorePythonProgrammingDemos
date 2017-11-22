#!/usr/bin/env python

"""Demo 8.1 for chapter 8."""

passwdList = ["123456", "654321", "111111"]
valid = False
count = 3
while count > 0:
    input = raw_input("Enter password:")

    # Check for valid password.
    for eachPasswd in passwdList:
        if input == eachPasswd:
            valid = True
            break

    if not valid:
        print "Invalid input."
        count -= 1
        continue
    else:
        print "Thank you for trying!"
        break
