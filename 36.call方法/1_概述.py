#!/usr/bin/env python
# -*- coding:utf8 -*-
# author:mafei0728


#语法

class Class:
    def __init__(self,name):
        self.name = name

    def __call__(self, *args, **kwargs):
        print("callable")


#一般对象实例化后,只能调用属性,但是类中有了call方法,就可以加括号运行了

c1 = Class("mafei0728")
c1()
print(callable(c1))
print(Class.__bases__)
# type是类的类,他是用来产生类的,它是元类
print(Class.__dict__)