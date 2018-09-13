#!/usr/bin/env python
# -*- coding:utf8 -*-
# author:mafei0728
x = 10000000
def fun1():
    print(x)
    def fun2():
        x=200000
        print(x)
    return fun2

f = fun1()
print(f)
f()