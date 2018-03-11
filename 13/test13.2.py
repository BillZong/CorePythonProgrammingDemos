#!/usr/bin/env python

"""Test demo 13.2 for chapter 13."""


class MyClass(object):
    """Simple class definition."""

    myVersion = 0.1  # class property

    def __init__(self):
        """Init."""
        super(MyClass, self).__init__()

    def show_my_version(self):
        """Show out my version."""
        print("{0} version is {1}".
              format(self.__class__.__name__,
                     self.__class__.myVersion))
    # format(MyClass.__name__,
    #        MyClass.myVersion))


print dir(MyClass)
print MyClass.__dict__
print ''

my_instance = MyClass()
my_instance.show_my_version()


class MySubClass(MyClass):
    """Sub class of simple class."""

    def __init__(self):
        """Init."""
        super(MySubClass, self).__init__()

    def show_my_super_class(self):
        """Show out my super class's name."""
        print("{0}'s bases is: {1}".
              format(self.__class__.__name__,
                     self.__class__.__bases__))

my_sub_instance = MySubClass()
my_sub_instance.show_my_super_class()
print ''

ret = isinstance(my_sub_instance, MyClass)
judgement = ""
if ret:
    judgement = "is"
else:
    judgement = "isn't"

print("my_sub_instance {0} a {1} instance.".
      format(judgement,
             MyClass.__name__))
