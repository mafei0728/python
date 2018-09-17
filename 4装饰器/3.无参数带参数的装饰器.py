#!/usr/bin/env python
# -*- coding:utf8 -*-
# author:mafei0728
import time
def fun1(fun):
    def fun2(*args,**kwargs):
        start_time = time.time()
        res = fun(*args,**kwargs)
        stop_time = time.time()
        print('run is %s ' %(stop_time-start_time))
        return res
    return fun2

@fun1 # fun3=fun2 传给3的参数其实就是传给2的参数
def fun3(name):
    time.sleep(1)
    print('ok,%s'%name)
    return 5

fun3('mafei')