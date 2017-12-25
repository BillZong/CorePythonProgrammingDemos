#!/usr/bin/env python

"""Demo 9.1 for chapter 9."""

import os

for tmpdir in ('/tmp', r'c:\temp'):
    if os.path.isdir(tmpdir):
        break
    else:
        print 'No temp directory available.'
        tmpdir = ''

if tmpdir:
    os.chdir(tmpdir)

cwd = os.getcwd()
print '*** Current temporary directory'
print cwd

print '*** Creating example directory'
if not os.path.exists('example'):
    os.mkdir('example')
os.chdir('example')
cwd = os.getcwd()
print '*** New working directory'
print cwd
print '*** Original diretory listing:'
print os.listdir(cwd)

print '*** Creating test file...'
fobj = open('test', 'w')
fobj.write('foo\n')
fobj.write('bar\n')
fobj.close()
print '*** Updated directory listing:'
print os.listdir(cwd)

path = os.path.join(cwd, os.listdir(cwd)[0])
print '*** Full file pathname'
print path
print '*** (pathname, basename) =='
print os.path.split(path)
print '*** (filename, extension) =='
print os.path.splitext(os.path.basename(path))

print '*** Displaying file contents:'
fobj = open(path)
for eachLine in fobj:
    print eachLine,
fobj.close()

print '*** Deleting test file'
os.remove(path)
print '*** Updated directory listing:'
print os.listdir(cwd)
os.chdir(os.pardir)
print '*** Deleting test directory'
os.removedirs('example')
print '*** Done'
