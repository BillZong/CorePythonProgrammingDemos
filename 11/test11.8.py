#!/usr/bin/env python

"""Test demo 11.8 for chapter 11."""

from random import randint


def simple_gen():
    """Simplest generators."""
    yield 1
    yield '2 --> punch!'

# myG = simple_gen()
# print myG.next()
# print myG.next()
# print myG.next()

for eachItem in simple_gen():
    print eachItem
print ''


def rand_gen(a_list):
    """Random length element generators."""
    while len(a_list) > 0:
        yield a_list.pop(randint(0, len(a_list) - 1))

for eachItem in rand_gen(['sax', 'rock', 'panel', 'paper', 'water']):
    print eachItem
print ''


def counter(start_at=0):
    """Counter never stop until you call close()."""
    count = start_at
    while True:
        val = yield count
        if val is not None:
            count = val
        else:
            count += 1

count = counter(5)
print count.next()
print count.next()
print count.send(9)
print count.next()
count.close()
print count.next()
