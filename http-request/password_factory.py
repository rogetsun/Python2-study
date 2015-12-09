# coding:utf-8

import hashlib

__author__ = 'uv2sun'

from time import ctime

passwd = "a1b2c3d4e5f6g7h8i9j0klmnoplrstuvwxyz"
# passwd = "1234567890"
passwd_len = 8
passwd_idx = []


def get_passwd():
    if not passwd_idx:
        passwd_idx.append(0)
    else:
        tf = False

        for i in range(len(passwd_idx)):
            idx = passwd_idx[(i + 1) * -1]
            if idx >= len(passwd) - 1:
                passwd_idx[(i + 1) * -1] = 0
            else:
                passwd_idx[(i + 1) * -1] += 1
                tf = True
                break
        if not tf:
            if len(passwd_idx) >= passwd_len:
                return False
            else:
                passwd_idx.append(0)
    return "".join([passwd[i] for i in passwd_idx])  #


# print ctime()
# while True:
#     pd = get_passwd()
#     if not pd:
#         break
#
# print ctime()
a = '19850128'
print hashlib.new('md5', hashlib.new('md5', a).hexdigest()).hexdigest()
