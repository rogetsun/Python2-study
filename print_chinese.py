# coding:utf-8
__author__ = 'uv2sun'

fp = open('chinese.txt', 'rb')
lines = fp.readlines()
print lines

a = lines[0].replace('\n', '')

print a

a = bytes('路透社')

print a

a = '\u123e\u743e\u932a'
print a
print a.decode('unicode-escape')

o = {'name': u'离退休'}
print o
