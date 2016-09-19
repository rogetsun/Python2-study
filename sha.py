# coding:utf-8

import hashlib
import urllib2

sh = hashlib.sha256()
# sh.update('https://www.python.org/ftp/python/3.5.1/Python-3.5.1.tar.xz')
p3 = open("/Users/uv2sun/Downloads/Python-3.4.4.tar.xz")
s = p3.read()
print s.__len__()
sh.update(s)
sha256 = sh.hexdigest()
print sha256
