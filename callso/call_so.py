# coding:utf-8
__author__ = 'uv2sun'
from ctypes import cdll
import os

print(os.getcwd())
sender = cdll.LoadLibrary(os.getcwd() + "/libxycom.so")

