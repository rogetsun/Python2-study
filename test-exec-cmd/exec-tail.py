# coding:utf-8
import commands

__author__ = 'uv2sun'

s = commands.getoutput('tail -n 100 /Users/uv2sun/Workspaces/PyCharm/PM/server/log/sm.log')
print s
