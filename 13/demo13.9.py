#!/usr/bin/env python
# encoding: UTF-8

"""Demo 13.9 for chapter 13."""

import os
import pickle


class FileDescr(object):
    """docstring for FileDescr."""

    saved = []

    def __init__(self, name=None):
        """Init."""
        self.name = name

    def __get__(self, obj, typ=None):
        """Get descriptor."""
        if self.name not in FileDescr.saved:
            raise AttributeError("%r used before assignment"
                                 % self.name)

        try:
            f = open(self.name, 'r')
            val = pickle.load(f)
            f.close()
            return val
        except (TypeError, pickle.PickleError):
            raise AttributeError("could not pickle %r" % self.name)
        finally:
            f.close()

    def __set__(self, obj, val):
        """Set descriptor."""
        f = open(self.name, 'w')
        try:
            try:
                pickle.dump(val, f)
                FileDescr.saved.append(self.name)
            except:
                pass
        except (TypeError, pickle.PicklingError):
            raise AttributeError("could not pickle %r" % self.name)

    def __delete__(self, obj):
        """Delete descriptor."""
        try:
            os.unlink(self.name)
            FileDescr.saved.remove(self.name)
        except (OSError, ValueError):
            print("The file(%r) try to removed is not exist",
                  self.name)


class MyFileVarClass(object):
    """docstring for MyFileVarClass."""

    foo = FileDescr('foo')
    bar = FileDescr('bar')


if __name__ == '__main__':
    fvc = MyFileVarClass()
    try:
        print fvc.foo
    except AttributeError, e:
        print("{0}".format(e))
    finally:
        print ''

    try:
        fvc.foo = 42
        fvc.bar = 'leanna'
        print fvc.foo
        print fvc.bar
    except AttributeError, e:
        print("{0}".format(e))
    finally:
        print ''

    try:
        del fvc.foo, fvc.bar
        print fvc.foo, fvc.bar
    except AttributeError, e:
        print("{0}".format(e))
    finally:
        print ''
