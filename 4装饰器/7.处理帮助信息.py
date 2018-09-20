#!/usr/bin/env python
# -*- coding:utf8 -*-
# author:mafei0728
import time
from functools import wraps
def fun1(fun):
    @wraps(fun) ##此处加装饰器,指定是显示原函数的帮助信息
    def fun2(*args,**kwargs):
        '''ok'''
        start_time = time.time()
        res = fun()
        stop_time = time.time()
        print('run %s'%(stop_time-start_time))
        return res
    return fun2


@fun1
def fun():
    '''test'''
    time.sleep(1)
    print('ok')
    return 1

fun()
print(fun.__doc__)