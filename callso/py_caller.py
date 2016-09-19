# coding:utf-8
__author__ = 'uv2sun'
from ctypes import cdll
from sys import argv


def send_file(so_file, url, src_file, dest_file):
    lib = cdll.LoadLibrary(so_file)
    r = lib.sendfile(url, src_file, dest_file)
    # print("%s, %s,%s,%s" % (so_file, url, src_file, dest_file))
    return 1


if __name__ == "__main__":
    if argv.__len__() != 5:
        print (9)
    else:
        so_file = argv[1]
        url = argv[2]
        src_file = argv[3]
        dest_file = argv[4]
        ret = send_file(so_file, url, src_file, dest_file)
        print(ret)
