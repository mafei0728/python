#!/usr/bin/env python
# -*- coding:utf8 -*-
# author:mafei0728
def fun1(x):
    while x>0:
        print('ok')
        yield x
        x -= 1

y = fun1(10)

for i in y:
    print(i)