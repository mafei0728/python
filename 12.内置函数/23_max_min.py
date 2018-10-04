#!/usr/bin/env python
# -*- coding:utf8 -*-
# author:mafei0728



#普通用法
print(max([1,2,4,5,667]))
print(min([1,2,4,5,667]))

a={
    "a":111,
    "b":222,
    "c":3333,
    "d":333322,
}

#先将a变成迭代器,next(a)一个值传给后面的函数来比较,取出最大值的next(a)
print(max(a,key=lambda k:a[k]))
print(min(a,key=lambda k:a[k]))