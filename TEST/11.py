#!/usr/bin/env python
# -*- coding:utf8 -*-
# author:mafei0728
def ppp(sum_m):
    t = 0
    s = 0
    t  = sum_m // 2
    s  = sum_m // 2
    p = s
    g = s
    while p//2:
        s = p //2 + g //4
        t +=s
        p = s + p%2
        g = s + g%4
    return t,p,g

print(ppp(10))