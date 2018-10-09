#!/usr/bin/env python
# -*- coding:utf8 -*-
# author:mafei0728

#把对象按照字典的形式来操作.分别触发

class Class:
    def __init__(self,name):
        self.name = name

    def __setitem__(self, key, value):
        self.__dict__[key] = value

    def __getitem__(self, item):
        return self.__dict__[item]

    def __delitem__(self, key):
        self.__dict__.pop(key)


c1 = Class("mafei0728")

print(c1["name"])
c1["age"] = 9999999999999999999
print(c1.__dict__)

del c1['age']

print(c1.__dict__)

# 记得跟上面的3个函数区分开,上面是,直接操作对象的属性,这个是当做字典来操作