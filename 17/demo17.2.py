#!/usr/bin/env python
# encoding: UTF-8

"""Demo 17.2 for chapter 17."""

# NNTP 下载示例 (getFirstNNTP.py)
# 这个脚本下载并显示 Python 新闻组 comp.lang.python 最后一篇文章的前 20 个“有意义的”行。

import nntplib
import socket

HOST = 'news.newsfan.net'
HOST = 'your.nntp.server'
GRNM = 'comp.lang.python'
USER = 'wesley'
PASS = "you'llNeverGuess"


def main():
    """Main function."""
    def display_first20(data):
        """Display first 20 meaningful lines."""
        print '*** First (<= 20) meaningful lines:\n'
        count = 0
        lines = (line.rstrip() for line in data)
        last_blank = True
        for line in lines:
            if line:
                lower = line.lower()
                if (lower.startswith('>') and \
                    (not lower.startswith('>>>'))) or \
                    lower.startswith('|') or \
                    lower.startswith('in article') or \
                    lower.endswith('writes:') or \
                    lower.endswith('wrote:'):
                    continue

                if not last_blank or (last_blank and line):
                    print ' %s' % line
                if line:
                    count += 1
                    last_blank = False
                else:
                    last_blank = True
                if count == 20:
                    break

    try:
        n = nntplib.NNTP(HOST)
        # ,user=USER, password=PASS)
    except socket.gaierror, e:
        print 'ERROR: cannot reach host "%s"' % HOST
        # print ' ("%s")' % eval(str(e))[1]
        print ' ("%s")' % str(e)
        return
    except nntplib.NNTPPermanentError, e:
        print 'ERROR: access denied on "%s"' % HOST
        print ' ("%s")' % str(e)
        return
    print '*** Connected to host "%s"' % HOST

    try:
        rsp, ct, fst, lst, grp = n.group(GRNM)
    except nntplib.NNTPTemporaryError, e:
        print 'ERROR: cannot load group "%s"' % GRNM
        print ' ("%s")' % str(e)
        print ' Server may require authentication'
        print ' Uncomment/edit login line above'
        n.quit()
        return
    except nntplib.NNTPTemporaryError, e:
        print 'ERROR: group "%s" unavailable' % GRNM
        print ' ("%s")' % str(e)
        n.quit()
        return
    print '*** Found newsgroup "%s"' % GRNM

    rng = '%s-%s' % (lst, lst)
    rsp, frm = n.xhdr('from', rng)
    rsp, sub = n.xhdr('subject', rng)
    rsp, dat = n.xhdr('date', rng)
    print '''*** Found last article (#%s):

From: %s
Subject: %s
Date: %s
''' % (lst, frm[0][1], sub[0][1], dat[0][1])

    rsp, anum, mid, data = n.body(lst)
    display_first20(data)
    n.quite()


if __name__ == '__main__':
    main()
