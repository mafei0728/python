#!/usr/bin/env python
# -*- coding:utf8 -*-
# author:mafei0728


#身份判断,说内存地址是不准确的

a=11
b=11
print(id(a))
print(id(b))
print(id(type(a)))
print(id(int))
#但是python2类型太大也会不一样,3不会了
c=121212121212121211111111111111111111111111111111111111111111111111
d=121212121212121211111111111111111111111111111111111111111111111111
print(id(c))
print(id(d))
