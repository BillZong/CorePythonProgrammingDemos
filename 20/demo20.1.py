#!/usr/bin/env python
# encoding: UTF-8

"""Demo 20.1 for chapter 20."""

# HTTP Auth Client (urlopenAuth.py)
# This script uses both techniques described above for basic authentication.

import urllib2

LOGIN = 'xxx@oudmon.com'
PASSWD = "xxxxxxxx"
URL = 'http://mail.abc.com/'


def handler_version(url):
    """Handler."""
    from urlparse import urlparse as up
    hd1r = urllib2.HTTPBasicAuthHandler()
    hd1r.add_password('Archives', up(url)[1], LOGIN, PASSWD)
    opener = urllib2.build_opener(hd1r)
    urllib2.install_opener(opener)
    return url


def request_version(url):
    """Request."""
    from base64 import encodestring
    req = urllib2.Request(url)
    b64str = encodestring('%s:%s' % (LOGIN, PASSWD))[:-1]
    req.add_header('Authorization', "Basic %s" % b64str)
    return req

for funcType in ('handler', 'request'):
    print '*** Using %s:' % funcType.upper()
    url = eval('%s_version' % funcType)(URL)
    f = urllib2.urlopen(url)
    print f.readline()
    f.close()
