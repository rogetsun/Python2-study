# coding:utf-8
import time

from MyThread import MyThread

__author__ = 'uv2sun'

t1 = MyThread(1, "t1")
t2 = MyThread(2, "t2")
print time.ctime()
t1.start()
t2.start()

t1.join()
t2.join()

print time.ctime()


