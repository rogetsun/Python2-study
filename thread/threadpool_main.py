# coding:utf-8
import threadpool
from multiprocessing import cpu_count

import time

import thread

__author__ = 'uv2sun'


def my_deal(a, b, c, **kw):
    print "%s begin to run %s %s\n" % (a, b, c)
    print kw
    time.sleep(2)
    print "%s end\n" % a


print cpu_count()
pool = threadpool.ThreadPool(cpu_count())

rs = threadpool.makeRequests(my_deal, [((i, i, i)) for i in range(10)])

[pool.putRequest(r) for r in rs]

#
# time.sleep(2)
# rs = threadpool.makeRequests(my_deal, [i + 10 for i in range(10)])
# [pool.putRequest(r) for r in rs]

pool.wait()

