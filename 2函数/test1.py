#!/usr/bin/env python
# -*- coding:utf8 -*-
# author:mafei0728
def name():
    '''pass'''
    pass
def func1():
    '''testing'''
    print("in the func1")
    return 0
#过程(就是没有返回值的函数)
def func2():
    '''testing2'''
    print("in the func2")
x=func1()
y=func2()
print("return from fun1 is %s" %x)
print("return from fun2 is %s" %y)