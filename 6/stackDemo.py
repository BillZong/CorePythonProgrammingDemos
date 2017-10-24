#!/usr/bin/env python

"""Stack demo for chapter 6."""

stack = []


def pushit():
    """Push of an element."""
    stack.append(raw_input('Enter new string: ').strip())


def popit():
    """Pop of an element."""
    if len(stack) == 0:
        print 'Can\'t pop from an empty stack!'
    else:
        print 'Remove ["%s"]' % stack.pop()


def viewstack():
    """Print stack."""
    print stack


CMDs = {'u': pushit, 'o': popit, 'v': viewstack}


def show_menu():
    """Menu to show."""
    pr = """
    p(U)sh
    p(O)p
    (V)iew
    (Q)uit

    Enter choice: """

    while True:
        while True:
            try:
                choice = raw_input(pr).strip()[0].lower()
            except(EOFError, KeyboardInterrupt, IndexError):
                choice = 'q'

            print '\nYou picked: [%s]' % choice
            if choice not in 'uovq':
                print 'Invalid option, try agin'
            else:
                break

        if choice == 'q':
            break
        CMDs[choice]()

if __name__ == '__main__':
    show_menu()
