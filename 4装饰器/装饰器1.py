#!/usr/bin/env python
# -*- coding:utf8 -*-
# author:mafei0728
import time
def fun1(fun):
    start_time = time.time()
    fun()
    stop_time = time.time()
    print('run is %s'%(stop_time -start_time))
    return fun

@fun1  ###这个地方的意思时间上是 fun2 = fun1(fun2)
def fun2():
    time.sleep(1)
    print('ok')
    return 1
###这种写法不对
#加上@ 在调用fun2()的时候.先执行fun1(fun2),在把fun2返回给fun2,fun2()在执行,相当于执行了两次
fun2()