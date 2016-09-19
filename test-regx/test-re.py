# coding:utf-8
__author__ = 'uv2sun'
import re

regx = re.compile('\s*')

s = 'a\nb\nc\n\nd'

ret = re.findall('(\w+)\s?', s)
print ret
print s.split('\n')
