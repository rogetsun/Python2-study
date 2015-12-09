# coding:utf-8
__author__ = 'uv2sun'

json = [
    {'id': 1, 'name': 'n1'},
    {'id': 2, 'name': 'n2'},
    {'id': 3, 'name': 'n3'}
]

print('%s' % (u.get('id') for u in json))

print int(-1L)
print type(-1L)
a = '-1'
print int(a)
