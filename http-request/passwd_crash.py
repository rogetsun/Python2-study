# coding:utf-8
import time
from time import ctime

__author__ = 'uv2sun'

from Http import post
import threadpool
from Queue import Queue
from password_factory import get_passwd
import threading
import hashlib
import json

my_queue = Queue(100)
pd_queue = Queue(1)

password = "d9b1d7db4cd6e70935368a1efb10e377"


def crack_passwd():
    print "begin to crack password"
    count = 0
    while True:
        count += 1
        if count % 1000000 == 0:
            print "deal %d" % (count,)
        pass_wd = my_queue.get()
        if pass_wd:
            # res = post("/login", {"login_no": "songyw@163.com", "login_password": m.hexdigest(), "remeber_me": "0"})
            # if json.loads(res).get("ret_code") == "0":
            #     pd_queue.put(pass_wd)
            #     break
            if hashlib.new('md5',
                           hashlib.new('md5', pass_wd).hexdigest()
                           ).hexdigest() == password:
                pd_queue.put(pass_wd)
                break
        else:
            print "over failure"
            break


def create_passwd():
    global my_queue
    while True:
        pd = get_passwd()
        if not pd:
            break
        my_queue.put(pd)


t1 = threading.Thread(target=create_passwd, name="create_password1")
t2 = threading.Thread(target=crack_passwd, name="crack_passwd1")
t3 = threading.Thread(target=crack_passwd, name="crack_passwd2")
t4 = threading.Thread(target=crack_passwd, name="crack_passwd3")
t1.setDaemon(True)
t2.setDaemon(True)
t3.setDaemon(True)
t4.setDaemon(True)
print ctime()
t1.start()
t2.start()
t3.start()
t4.start()

pd = pd_queue.get()
print ctime()
print pd
