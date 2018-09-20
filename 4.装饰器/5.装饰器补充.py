#!/usr/bin/env python
# -*- coding:utf8 -*-
# author:mafei0728
#一个函数可以有多个装饰器
def fun1(fun):
    pass

def fun2(fun):
    pass

def fun3(fun):
    pass



###多个装饰器,重里到外开始执行,道理都一样
@fun3
@fun2
@fun1
def fun():
    pass