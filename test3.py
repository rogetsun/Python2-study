__author__ = 'uv2sun'
import site

print site.getsitepackages()

try:
    import wx
except Exception as e:
    print Exception, e

print wx.version()

import cefpython3

print cefpython3.__version__

try:
    import json

    json.loads()
except Exception as e:
    print Exception, ':', e
