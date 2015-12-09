# coding:utf-8
import struct

__author__ = 'uv2sun'

import time
import binascii

t = time.time()
print t

print 2 ** 32

print int(t) >> 24

print int(t) >> 24 << 24 | 2 ** 24

print time.localtime(int(t) >> 24 << 24 | 2 ** 24 - 1)
print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(t) >> 24 << 24 | 2 ** 24 - 1))
print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(85 << 24 | 2 ** 24 - 1))
print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(84 << 24 | 2 ** 24 - 1))
print bin(2 ** 2 - 1)

print int(bin(3)[2:], 16)
print ord('a')

b = struct.pack("!i", 259)
print binascii.hexlify(b)
s = struct.unpack('BB2s', b)[2]
print repr(s)
print struct.unpack('!H', s)[0]
"""
    00000100
    0,0,1,0
"""
print '**********'

b = 1.3.hex()
print b
b = struct.pack('!f', -1.5)
print b
print '%.2f' % struct.unpack('!f', b)
print type(struct.unpack('!f', b)[0])

print '**********'

t = time.time()

b = struct.pack('!I', t)
print repr(b)
hi = struct.unpack('!B3s', b)[0]
print hi

print int('111111111111111111111111', 2)
print hex(3)

print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(86 << 24 | int('111111111111111111111111', 2)))
