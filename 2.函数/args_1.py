#!/usr/bin/env python
# -*- coding:utf8 -*-
# author:mafei0728
def fun1(x,*args):
    print(args)
    print(args)

def fun2(x,y,t=5,**kwargs):
    print(x)
    print(kwargs)
    print(t)


fun2(2,2,z=1,t=3)