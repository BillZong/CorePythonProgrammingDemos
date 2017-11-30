#!/usr/bin/env python

"""Test demo 8.2 for chapter 8."""

myTuple = (123, 'xyz', 45.67)
i = iter(myTuple)
while True:
    try:
        print i.next()
    except StopIteration:
        break
print ""

legends = {('Poe', 'author'): (1809, 1849, 1976),
           ('Gaudi', 'architect'): (1852, 1906, 1987),
           ('Freud', 'psychoanalyst'): (1856, 1939, 1990)
           }
for eachLegend in legends:
    print 'Name: %s\tOccupation: %s' % eachLegend
    print 'Birth: %s\tDeath: %s\tAlbum: %s\n' \
        % legends[eachLegend]
print ""

myFile = open('config-win.txt')
for eachLine in myFile:
    print eachLine,  # comma suppresses extra \n
