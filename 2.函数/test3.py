#!/usr/bin/env python
# -*- coding:utf8 -*-
# author:mafei0728
def fun(a,b):
    c = type(a)
    if c is list:
        a.append(b)
    if c is str:
        a=a+b
    if c is int:
        a = a+9
    print(a)
x=[1,2,4]
y="c"
fun(x,y)
print(x)

g = "a"
f = 'b'
fun(g,f)
print(g)

h = 1
j = 2
fun(h,f)
print(h)