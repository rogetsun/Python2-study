__author__ = 'uv2sun'
from datetime import datetime
import time
import struct

print time.time()

print time.tzname
dt = datetime.now()
print dt

print dt.timetuple()

print time.mktime(dt.timetuple())

print time.localtime(time.mktime(dt.timetuple()))

t = 1434343434L

print time.localtime(t)

t = time.time()
b = struct.pack("!I", t)
print [hex(i) for i in struct.unpack("!BBBB", b)]
