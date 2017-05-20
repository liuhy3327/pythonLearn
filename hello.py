# -*- coding: utf-8 -*-
import  xml.dom.minidom
import os
import os.path
import gzip

def GetFileList(dir, fileList):
    newDir = dir
    if os.path.isfile(dir):
    	fileList=[2]
    elif os.path.isdir(dir):
    	fileList=[1]
    return fileList

dir='C:\\Users\\Administrator\\Desktop\work_file\\py-cloud-project\\py-cloud-project\\resources'

print(GetFileList(dir, []))

dom = xml.dom.minidom.parse("C:\\Users\\Administrator\\Desktop\\export-src-ods-bill.xml")
root = dom.documentElement


f=open('f.txt','a')
dbtn = root.getElementsByTagName('dbtn')
for x in dbtn:
	print(x.firstChild.data)
	f.write(x.firstChild.data)
	f.write('\n')
f.close()



