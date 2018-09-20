#!/usr/bin/env python
# -*- coding:utf8 -*-
# author:mafei0728
def fun1(local):
    def fun2(fun):
        def fun3(*args,**kwargs):
            if local == 'x':
                print('x')
                res = fun(*args,**kwargs)
                return res
            elif local == "y":
                print('y')
                res = fun(*args,**kwargs)
                return res
        return fun3
    return fun2

@fun1(local='x')
def ll():
    pass