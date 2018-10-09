#!/usr/bin/env python
# -*- coding:utf8 -*-
# author:mafei0728

# 前面理解了元类,__call__,现在来看下实例化过程,控制实例化的过程

class Meta_lass(type):
    def __init__(self,class_name,class_bases,class_dict):
        pass  #<===================================这里不用写type里面也会实现

    def __call__(self, *args, **kwargs):  #<======理解元类实例化对象的过程
        obj = self.__new__(self) # <======通过类通过__new__产生一个空对象,只穿类,产生空对象.也可以穿其他的直接产生对象
        self.__init__(obj,*args,**kwargs) # <======在调用类下面的__init__方法
        return obj  #<=====返回obj对象



class Class(metaclass=Meta_lass):
    def __init__(self,name):
        self.name = name

    def fun1(self):
        print("ok")

#我们之前学了__call__我们知道,当我们对象加()的时候,实际上是调用了类的__call__方法,当我们把类当对象,实例化对象的时候.其实也是调元类的__call_方法
c1 = Class("mafei0728")
print(c1.name)