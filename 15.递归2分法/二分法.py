#!/usr/bin/env python
# -*- coding:utf8 -*-
# author:mafei0728
import random
a=[]
for i in range(400):
    i=random.randint(0,40000)
    a.append(i)
date=sorted(a)
print(date)
num=input("请输入一个数组:")
num=int(num)
count_1=0
date=[1,2,3]
def fun1(num,date,count_1):
    count_1+=1
    l1=len(date)
    if  l1 == 1 and num != date[0]:
        print('不在里面,找了.%s'%count_1)
        return date
    if  num == date[l1//2]:
        print(date)
        print('找到了....找了.%s'%count_1)
        return date
    if  num > date[l1//2]:
        date=date[l1//2:]
        return fun1(num,date,count_1)
    if  num < date[l1//2]:
        date = date[:l1//2]
        return fun1(num, date,count_1)



fun1(num,date,count_1)