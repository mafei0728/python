#!/usr/bin/env python
# -*- coding:utf8 -*-
# author:mafei0728



#复数
a=1+2j #根下面一样
x = complex(1-2j)
print(x.real)
print(x.imag)

#
# ###数据类型
# list
# tuple
# set
# frozenset #不可变集合
# int
# str
# bool
# dict

# #####扩展,适用于所有类型######
# c=1
# #身份判断
# print(type(c) is int)
# #标准身份判断
# print(isinstance(c,int))
# #is 一般通过id来判断
# print(c is 2)