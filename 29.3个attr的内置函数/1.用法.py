#!/usr/bin/env python
# -*- coding:utf8 -*-
# author:mafei0728

class Class1:
    def __init__(self,name):
        self.name = name


    # 操作字符串属性的时候就会通过字符串的形式操作
    def __setattr__(self, key, value):
        if not isinstance(value,str):
            raise TypeError("type Error" )  #<---这样可以统一限制传入类型,我们可以自定义很多操作
        self.__dict__[key] = value   # <----------------主要步骤

    def __getattr__(self, item): # <-------------属性不存在的情况下才会触发运行,这是对象查找的终点,当这边没有定义的时候,则抛出异常,这边有定义的时候
         return 4                                 #抛出返回值

    def __delattr__(self, item):
        self.__dict__.pop(item) # <------------删除类属性的本质操作,这里也可以做一些操作限制删除


c1 = Class1("mafei0728")
print(c1.__dict__)
print(c1.name)
del c1.name
print(c1.name)
print(c1.aa)
#c2 = Class1(1111)

# 总结:del ,set 可以限制属性的操作,类似property单体输出,这个是AOE输出 ,get用法比较特别.而且用的比较多,很重要.