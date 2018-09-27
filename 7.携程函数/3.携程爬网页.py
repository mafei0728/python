#!/usr/bin/env python
# -*- coding:utf8 -*-
# author:mafei0728
from urllib.request import urlopen
def next_1(fun):
    def fun1(*args,**kwargs):
        init1=fun(*args,**kwargs)
        next(init1)
        return init1
    return fun1



@next_1
def get():
    while True:
        url = yield
        res = urlopen(url).read()
        print(res)

a = get()
a.send('http://172.16.30.32')