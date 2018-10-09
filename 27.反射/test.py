#!/usr/bin/env python
# -*- coding:utf8 -*-
# author:mafei0728

#反射模块

import sys,time

class Class:
    pass


def fun1():
    print("x")

def fun2():
    print("y")

def fun3():
    print("z")

### 判断该操作是在模块还是在当前文件中
print(__name__)
#比如,下面的操作在其他人导入这个模块是不会执行的,一般可以用于本模块的执行,或者主程序中
if __name__ == "__main__":
    print("x")

### 一切皆对象,当我们要通过反射操作我们当前文件这个对象时候,可以通过下面这来玩

m1 = sys.modules[__name__]
print(m1)
print(hasattr(m1,"Class"))
print(hasattr(m1,"fun1"))
print(hasattr(m1,"fun2"))
print(hasattr(m1,"fun3"))