#!/usr/bin/env python
# -*- coding:utf8 -*-
# author:mafei0728
# f = open('sweet')
# g = open('test1','w')
# for i in f:
#     if i.strip():
#         g.write(i)
# f = open('test2',encoding='gbk')
# g = open('test3','w',encoding='utf8')
# for i in f:
#     if i.startswith('每四年'):
#        i = ''.join([i.strip(),'马飞','\n'])
#     g.write(i)
f = open('test3',encoding='utf8')
for index,line in enumerate(f,1):
    if 2<= index <=5:
        print(index,line.strip())