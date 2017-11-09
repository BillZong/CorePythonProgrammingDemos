#!/usr/bin/env python

"""Demo 6.2 for chapter 6."""

from string import Template
import re


print 'Hello' + u' ' + 'World' + u'!'
print 'Hello ' * 20
print ""

print 'There are %(howmany)d %(lang)s Quotation Symbos.' % \
    {'lang': 'Python', 'howmany': 3}
print ""

s = Template('Ther are ${howmany} ${lang} Quotation Symbols.')
print s.substitute(lang='Python', howmany=3)
print s.safe_substitute(lang='Python')
print ""

# print '\n'
# print r'\n'
# print ""

# m = re.search('\\[rtfvn]', r'Hello World!\n')
# if m is not None:
#     print m.group()

m = re.search(r'\\[rtfvn]', r'Hello World!\n')
if m is not None:
    print m.group()
print ""

print u'abc\u2463\n'
print ur'Hello\nWorld!'
print ""

s, t = 'foa', 'aos'
print zip(s, t)
print ""

print s.capitalize()
print s.center(30)
print s.count('a', 0, len(s))
print s.encode('UTF-8', 'strict')
print s.find('c', 0, len(s))
# print s.index('c', 0, len(s)) #ValueError
print '%s %s' % (s, t)
print ''
