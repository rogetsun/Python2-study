# coding:utf-8
__author__ = 'uv2sun'

from docx import Document

docu = Document('demo.docx')
tbls = docu.tables
print len(tbls)