#!/usr/bin/env python
# -*- coding:utf8 -*-
# author:mafei0728



a={
    "a":111,
    "b":222,
    "c":3333,
    "d":333322,
}

#调用,前面传 k,后面就是return
f=lambda k:a[k]
print(f("a"))



#匿名函数优点,什么时候调用,什么时候定义