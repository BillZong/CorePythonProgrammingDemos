#!/usr/bin/env python

'readTextFile.py -- read and display text file'

# import logging

# FORMAT = '%(asctime)-15s %(clientip)s %(user)-8s %(message)s'
# logging.basicConfig(format=FORMAT)
# d = {'clientip': '192.168.1.105', 'user': 'fbloggs'}
# logger = logging.getLogger('tcpserver')
# logger.warning('Protocol problem: %s', 'connection reset', extra=d)

#get filename
fname = raw_input('Enter filename:')
print

# attempt to open file for reading
try:
    logging.
    fobj = open(fname, 'r')
except IOError, e:
    print '*** file open error:', e
else:
    # display contents to the screen
    for eachLine in fobj:
        print eachLine,
    fobj.close()