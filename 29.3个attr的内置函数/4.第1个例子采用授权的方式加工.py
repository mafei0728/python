#!/usr/bin/env python
# -*- coding:utf8 -*-
# author:mafei0728

#用授权实现list,智能插入数字
class List:
    def __init__(self,seq):
        self.seq = list(seq)


    def append(self,values):
        if not isinstance(values,int):
            raise TypeError
        self.seq.append(values)


    #初此之前的方法,依照list原本方法
    def __getattr__(self, item):
        return getattr(self.seq,item)

    #打印实例的时候,去打印实例的seq,而不是对象的内存地址,实例化的时候,会触发下面这个函数返回值给对象
    def __str__(self):
        return  str(self.seq)

l1 = List([1,2,3,54,6])
#抛出错误
#l1.append("111")
#正常插入
l1.insert(0,1212)
#触发str
print(l1)