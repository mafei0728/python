#!/usr/bin/env python
# -*- coding:utf8 -*-
# author:mafei0728


#用类实现20以类的序列迭代器
class Class:
    def __init__(self,start):
        self.start = start


    def __iter__(self): #先实现可迭代
        return self


    def __next__(self): #实现迭代器
        if self.start > 20:
            raise StopIteration
        n = self.start
        self.start += 1
        return n

c1 = Class(0)
for i in c1:
    print(i)