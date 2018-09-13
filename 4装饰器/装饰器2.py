#!/usr/bin/env python
# -*- coding:utf8 -*-
# author:mafei0728
import time
def fun1(fun):
    def fun2():
        start_time = time.time()
        res = fun()
        stop_time = time.time()
        print('run is %s ' %(stop_time-start_time))
        return res
    return fun2

@fun1
def fun3():
    time.sleep(1)
    print('ok')
    return 5

#加上@,相当于执行fun1,把fun3=fun2 在执行fun3(),相当于执行fun2(),根本闭包的概念,里面的参数,是最早的fun3,完美
fun3()