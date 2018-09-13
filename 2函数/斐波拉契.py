#!/usr/bin/env python
# -*- coding:utf8 -*-
# author:mafei0728
def fun(n):
    a,b = 0,1
    while a < n:
        print(a,end=' ')
        a,b =b,a+b

fun(100)