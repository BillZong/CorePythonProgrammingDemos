#!/usr/bin/env python

"""Queue demo for chapter 6."""

queue = []


def enqueue():
    """Enqueue."""
    queue.append(raw_input('Enter new string: ').strip())


def dequeue():
    """Dequeue."""
    if len(queue) == 0:
        print 'Can\'t pop from an empty queue!'
    else:
        print 'Remove ["%s"]' % queue.pop(0)


def viewqueue():
    """Print of the queue."""
    print queue

CMDs = {'e': enqueue, 'd': dequeue, 'v': viewqueue}


def showmenu():
    """Show out he menu."""
    pr = """
    (E)nqueue
    (D)equeue
    (V)iew
    (Q)uit

    Enter the choice: """

    while True:
        while True:
            try:
                choice = raw_input(pr).strip()[0].lower()
            except(EOFError, KeyboardInterrupt, IndexError):
                choice = 'q'

            print '\nYou picked: [%s]' % choice
            if choice not in 'edvq':
                print 'Invalid option, try again'
            else:
                break

        if choice == 'q':
            break
        CMDs[choice]()

if __name__ == '__main__':
    showmenu()
