#!/usr/bin/env python

"""Demo 7.1 for Chapter 7."""

db = {}


def new_user():
    """Creation of a new user."""
    prompt = 'Login desired: '
    while True:
        name = raw_input(prompt)
        if name in db:
            prompt = 'Name taken, try another: '
            continue
        else:
            break
    pwd = raw_input('password: ')
    db[name] = pwd


def old_user():
    """Login of an old user."""
    name = raw_input('Login: ')
    if name not in db:
        print 'User not register.'
        return

    pwd = raw_input('Password: ')

    realpwd = db.get(name)
    if realpwd == pwd:
        print 'Welcome back', name
    else:
        print 'Wrong password.'


def show_menu():
    """Menu of login or register."""
    prompt = """
(N)ew User Register
(E)xist User Login
(Q)uit

Enter choice: """

    done = False
    while not done:
        chosen = False
        while not chosen:
            try:
                choice = raw_input(prompt).strip()
                if len(choice) == 0:
                    print '\n\nYou need to pick a choice'
                    continue
                choice = choice[0].lower()
            except (EOFError, KeyboardInterrupt):
                choice = 'q'
            print '\nYou picked: [%s]' % choice
            if choice not in 'neq':
                print 'Invalid option, try again'
            else:
                chosen = True
                done = True
    new_user()
    old_user()

if __name__ == '__main__':
    show_menu()
