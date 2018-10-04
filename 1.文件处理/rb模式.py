#!/usr/bin/env python
# -*- coding:utf8 -*-
# author:mafei0728
f = open('test1','rb+')
a=f.readline()
print(type(a))
print(a.decode(encoding='utf8'))
b = '\n马飞'
f.seek(0,2)
f.write(b.encode('utf8'))
