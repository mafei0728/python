#!/usr/bin/env python
# -*- coding:utf8 -*-
# author:mafei0728
####去掉文件前面的空格,应用
import os,sys
def init(fun):
    def fun1(*args,**kwargs):
        init1=fun(*args,**kwargs)
        next(init1)
        return init1
    return fun1

@init
def opener(target):
    while True:
        filename = yield
        with open(filename) as f:
            target.send((filename,f))

@init
def dispose(target):
    while True:
        filename,f = yield
        for i in f:
            line=i.strip()
            target.send((filename,line))

@init
def write1(new_file):
    while True:
        filename,line = yield
        with open(new_file,'a') as f:
            f.write(line+'\n')
            # target.send((filename,new_file))


def rename(new_file,filename):
    g = opener(dispose(write1(new_file)))
    g.send('test01')
    os.remove(filename)
    os.rename(new_file,filename)


#rename('test02','test01')


#简单的写法
def new(new_file,filename):
    with open(filename) as f:
        h = (line.lstrip() for line in f )
        with open(new_file,'a') as g:
            for i in h:
                g.write(i)
    os.remove(filename)
    os.rename(new_file,filename)

new('test02','test01')