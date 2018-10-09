#!/usr/bin/env python
# -*- coding:utf8 -*-
# author:mafei0728

class Wow:
    def attack(self,x):
        print(x)



    @staticmethod
    def version(x,y,z):
        print(x,y,z)



# 所谓静态方法就是类自己内部的一个普通函数,这个方法就是给类用的,类的工具包,对象也可以调用,但已经不是绑定方法,都指向同一个内存地址

w1 = Wow()

w1.attack(11)
w1.version(1,2,3)


#应用场景
import time
class Data:
    def __init__(self,year,month,day):
        self.year = year
        self.month = month
        self.day = day

    @staticmethod
    def today():
        t = time.localtime()
        obj = Data(t.tm_year,t.tm_mon,t.tm_mday)
        return  obj


##  通过静态方法来初始化函数
d1 =Data.today()
print(d1.year,d1.month,d1.day)