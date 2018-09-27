#!/usr/bin/env python
# -*- coding:utf8 -*-
# author:mafei0728
##模拟grep
import time
def receive(name):
    print('%s start working '%name)
    job_list=[]
    while True:
        job1=yield job_list
        print('%s receive a job,%s finishing this %s'%(name,name,job1))
        job_list.append(job1)
        print(job_list)
        time.sleep(1)


h1 = receive('jim')
next(h1)  ### 开始的时候不能用send 如果是 h1.send(None)==next(h1)
for i in range(10):
    h1.send('job%s'%i)  ### send除了有next的功能外,会吧一个值传给生成器里面的yield,函数返回的yield的值.传值和返回值不能搞混淆
