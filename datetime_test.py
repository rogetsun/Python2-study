__author__ = 'uv2sun'
from datetime import datetime
import time

print time.time()

print time.tzname
dt = datetime.now()
print dt

print dt.timetuple()

print time.mktime(dt.timetuple())

print time.localtime(time.mktime(dt.timetuple()))

t = 1434343434L

print time.localtime(t)
