#!/usr/bin/env python
# -*- coding:utf8 -*-
# author:mafei0728
x = 1
def fun1():
    x = 2
    y = 3
    def fun2():
        print(x)
        print(y)
    return fun2
f = fun1()
print(f)
#f就是一个闭包,引用了几个外部的变量,就包含几个元素
print(f.__closure__)
#通过下面的方法,可以打印出因为的具体变量值
print(f.__closure__[0].cell_contents)
print(f.__closure__[1].cell_contents)