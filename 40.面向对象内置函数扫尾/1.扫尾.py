#!/usr/bin/env python
# -*- coding:utf8 -*-
# author:mafei0728

class Class:
    '''xxxx'''
    def __init__(self,name):
        self.name = name


c1 = Class("mafei0728")


class Class1(Class):
    pass

# 打印注释信息,不能被继承
print(c1.__doc__)

#打印由哪个类产生的
print(c1.__class__)
print(Class.__class__)

#当前模块名
print(c1.__module__)
print(Class.__module__)


