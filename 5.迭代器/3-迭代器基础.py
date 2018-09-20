#!/usr/bin/env python
# -*- coding:utf8 -*-
# author:mafei0728
f = open('a.text','r')
f.__next__()
f.__iter__()
print(f)
print(f.__iter__())
#文件句柄既是可迭代对象,又是迭代器,其实和文件本身相等,所以可以直接用next方法
print(next(f).strip())
print(next(f).strip())
print(next(f).strip())
print(next(f).strip())
#优点
# 1: 迭代器提供了一种不依赖索引取值的方式
# 2: 不用把所有可迭代对象的元素放入内存,节省内存
#缺点
# 1: 无法统计对象的长度,使用不灵
# 2: 迭代器一次性,不能重复取值

#注意点
# 1: 迭代器使用__iter__后就是自己本身
# 2: 能用for循环则是是可迭代的,不一定是迭代器,必须通过iter()方法转换为迭代器