#!/usr/bin/env python
# -*- coding:utf8 -*-
# author:mafei0728
a = [1,2,3,4,5,6]
#一个对象如果有下面这个内置方法,就是可迭代对象
# 等同于iter(a),返回值称为迭代器
a.__iter__()
b = a.__iter__()
#等同于b=iter(a)
#a是可迭代对象,b是a的迭代器,迭代器有如下方法
print(b.__next__())
print(b.__next__())
print(b.__next__())
print(b.__next__())
#等同于next(b)
print(next(b))