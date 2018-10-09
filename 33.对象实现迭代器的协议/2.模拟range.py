#!/usr/bin/env python
# -*- coding:utf8 -*-
# author:mafei0728


#模拟rang
class Class:
    def __init__(self, range,start=0):
        self.range = range
        self.start = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.start  == self.range:
            raise StopIteration
        n = self.start
        self.start += 1
        return n


c1 = Class(100)
for i in c1:
    print(i)