#!/usr/bin/env python

"""Exercise answer 8.2 for chapter 8."""


def ui():
    """The program of UI."""
    while True:
        tip = """
Input three numbers, using ',' to seperate it.
These are from,to,and increment. We'll generate
a sequence for you. Using 'q' to quit this:
"""
        inp = raw_input(tip).strip()
        if inp == 'q':
            break
        else:
            nums = inp.split(',')
            if len(nums) != 3:
                print "Numbers not right."
                continue
            seq = xrange(int(nums[0]), int(nums[1]), int(nums[2]))
            for x in seq:
                print x,

if __name__ == '__main__':
    ui()
