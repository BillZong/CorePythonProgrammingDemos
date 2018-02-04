#!/usr/bin/env python

"""Demo 11.8 for chapter 11."""

from time import time


def logged(when):
    """Logger with time stamp."""
    def log(f, *args, **kargs):
        """Log with function, args, and key args."""
        print '''Called:
        function: %s
        args: %r
        kargs: %r''' % (f, args, kargs)

    def pre_logged(f):
        """Pre logger."""
        def wrapper(*args, **kargs):
            """Wrapper with pre logger."""
            log(f, *args, **kargs)
            return f(*args, **kargs)
        return wrapper

    def post_logged(f):
        """Post logger."""
        def wrapper(*args, **kargs):
            """Wrapper with post logger."""
            now = time()
            try:
                return f(*args, **kargs)
            finally:
                log(f, *args, **kargs)
                print "time delta: %s" % (time() - now)
        return wrapper

    try:
        return {"pre": pre_logged,
                "post": post_logged}[when]
    except KeyError, e:
        raise ValueError(e), 'must be "pre" or "post"'


@logged("post")
def hello(name):
    """Printing with an AOP function."""
    print "Hello,", name

hello("World!")
