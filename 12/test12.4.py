#!/usr/bin/env python

"""Demo 12.4 for chapter 12."""


def foo3():
    """Simple function for showing globals and locals."""
    print('\ncalling foo()...')
    a_string = 'bar'
    an_int = 42
    print("foo()'s globals:", globals().keys())
    print("foo()'s locals:", locals().keys())

print("__main__'s globals:", globals().keys())
print("__main__'s locals:", locals().keys())
foo3()
