#!/usr/bin/env python
# -*- coding:utf8 -*-
# author:mafei0728
import os
f = os.walk("D:\\临时存储软件\\Nagios监控安装包及客户端安装包")
#print(f)
for i in f:
    for k in i[-1]:
        filename='%s\\%s'%(i[0],k)
        print(filename)
        # with open(filename,encoding='gbk') as h:
        #     print(h.readlines())
        #     # if 'mysqld' in h:
        #     #     print(filename)

k = os.walk("D:\\临时存储软件\\Nagios监控安装包及客户端安装包")
l = ['%s/%s'%(i[0],g) for i in k for g in i[-1]]
print(l)