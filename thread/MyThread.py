# coding:utf-8
import time

from threadpool import WorkRequest, _handle_thread_exception

__author__ = 'uv2sun'

from threading import Thread


class MyThread(Thread):
    def __init__(self, id=None, name=None):
        super(MyThread, self).__init__()
        self.id = id
        self.name = name

    def run(self):
        print "[%s]%s is begin running" % (self.id, self.name)
        time.sleep(2)
        print "[%s]%s is end running" % (self.id, self.name)


t = "2002-04-22"
data = time.strptime(t, '%Y-%m-%d')
print data
data = time.mktime(data)
print data
now = time.time()
print now
print (now - data) / (60 * 60 * 24)
print time.localtime(data + (5000 * (60 * 60 * 24)))

print(isinstance((1, 2,), tuple))


def w(a, b, c, **kwargs):
    print a, b, c, kwargs
