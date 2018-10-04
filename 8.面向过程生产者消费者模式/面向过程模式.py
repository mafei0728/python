#!/usr/bin/env python
# -*- coding:utf8 -*-
# author:mafei0728
import time,os
def init(fun):
    '''init generator'''
    def fun1(*args,**kwargs):
        init1=fun(*args,**kwargs)
        next(init1)
        return init1
    return fun1


@init
def search(target):
    '''find file absolute path'''
    while True:
        file_path = yield
        h = os.walk(file_path)
        for i in h:
            for k in i[-1]:
                abs_file='%s\\%s'%(i[0],k)
                target.send(abs_file)


@init
def opener(target):
    '''open file'''
    while True:
        abs_file = yield
        with open(abs_file) as f:
            target.send((abs_file,f))


@init
def read_line(target):
    while True:
       abs_file,f = yield
       for line in f:
           target.send((abs_file,line))


@init
def filtration(pattern,target):
    '''filtration'''
    while True:
        abs_file,line = yield
        if pattern in line:
            target.send(abs_file)


@init
def printer():
    '''print res'''
    a=set({})
    while True:
        abs_file = yield
        print(abs_file)

a = search(opener(read_line(filtration('mysqld',printer()))))
a.send('C:\\11')
# 面向过程是流水线的编程思想,在设计程序的时候把整个流程设计出来
# 优点:
# 1.结构体系更加清晰47``
# 2.简化程序的复杂性
# 缺点:
# 1.可扩展性差,适合搞操作系统,这种不会大的更改的软件
# 2.