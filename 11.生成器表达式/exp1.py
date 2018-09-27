#!/usr/bin/env python
# -*- coding:utf8 -*-
# author:mafei0728
#优点:节省内存...一次内存一个值

list1 = ('name%s'%i for i in range(101))
print(next(list1))
print(next(list1))
print(next(list1))
print(next(list1))
print(next(list1))

