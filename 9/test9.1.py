#!/usr/bin/env python

"""Test demo 9.1 for chapter 9."""

import os

dir_files = os.walk("/Users/billzong/doc")

for file in dir_files:
    print file

print os.stat("/")

print os.major(os.stat("/").st_dev)
print os.minor(os.stat("/").st_dev)

print os.path.basename("/Users/billzong/doc")
print os.path.dirname("/Users/billzong/doc")
print os.path.join(
    os.path.dirname("/Users/billzong/doc"),
    os.path.basename("/Users/billzong/doc"))

print os.path.samefile(
    "/Users/billzong/doc/created.rid",
    "/Users/billzong/doc/test")
