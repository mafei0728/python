#!/usr/bin/env python
# -*- coding:utf8 -*-
# author:mafei0728
# f = open('test4','x',encoding='utf8')
# # f.write('ok')
# # f.write('ok')
# # f.write('ok')
f = open('test1','rb+')
f.seek(6)
print(f.tell())
f.seek(-2,1)
print(f.tell())
f.seek(-2,2)
c='abx'
a=c.encode('utf8')
f.write(a)
print(f.tell())
