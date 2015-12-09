__author__ = 'uv2sun'

from m1 import m1

print m1

fn = getattr(m1, 'test_getattr')
print fn

fn()
