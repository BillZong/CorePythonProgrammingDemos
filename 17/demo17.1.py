#!/usr/bin/env python
# encoding: UTF-8

"""Demo 17.1 for chapter 17."""

# FTP 下载示例 (getLatestFTP.py)
# 这个程序用于下载网站中最新版本的文件。你可以修改这个程序让它下载你喜欢的程序。

import ftplib
import os
import socket

HOST = 'ftp.mozilla.org'
DIRN = 'pub/webtools'
FILE = 'bugzilla-LATEST.tar.gz'


def main():
    """Main function."""
    try:
        f = ftplib.FTP(HOST)
    except (socket.error, socket.gaierror), e:
        print 'ERROR: cannot login anoymousely: %s' % e
        f.quit()
        return
    print '*** Logged in as "anoymous"'

    try:
        f.cwd(DIRN)
    except ftplib.error_perm:
        print 'ERROR: cannot CD to "%s"' % DIRN
        f.quit()
        return
    print '*** Changed to "%s" folder' % DIRN

    try:
        # 我们传了一个回调函数给 retrbinary()，它在每接收到一块二进制数据的时候都
        # 会被调用。这个函数就是我们创建的本地文件对应文件对象的 write 方法。
        # 在传输结束的时候，Python 解释器会自动关闭这个文件对象，而不会丢失数据。
        # 虽然这样方便，但最好还是不要这样做，做为 一个程序员，要尽量做到在资源不再
        # 被使用的时候就直接释放，而不是依赖其它代码来做释放操作。 在这里，我们应该
        # 把文件对象保存到一个变量中，如变量 loc，然后把 loc.write 传给
        # ftp.retrbinary()方法。
        f.retrbinary('RETR %s' % FILE, open(FILE, 'wb').write)
    except ftplib.error_perm:
        print 'ERROR: cannot read file "%s"' % FILE
        os.unlink(FILE)
    else:
        print '*** Downloaded "%s" to CWD' % FILE
    finally:
        f.quit()

if __name__ == '__main__':
    main()
