#!/usr/bin/env python
# -*- coding:utf8 -*-
# author:mafei0728
import time
def init(fun):
    def fun1(*args,**kwargs):
        init1=fun(*args,**kwargs)
        next(init1)
        return init1
    return fun1



@init
def receive(name):
    print('%s start working '%name)
    job_list=[]
    while True:
        job1=yield job_list
        print('%s receive a job,%s finishing this %s'%(name,name,job1))
        job_list.append(job1)
        print(job_list)
        time.sleep(1)

a = receive('kk')
a.send('aa')