#!/usr/bin/env python
# -*- coding:utf8 -*-
# author:mafei0728


# 类方法的基本语法
class Class1:
    def fun1(self):
        print("xx")


    @classmethod
    def fun(cls):
        print("yy")

# 类方式,指的是类的绑定方法,通过对对象的绑定方法,了解,我们能知道,当类调用类的绑定方法的时候,会自动把类传进去
# 这样类就能调类的属性,和实例化了
# 对象也能调用,自动传的是对象的类,调用手段一样,没啥意义


# __str__(self)方法
class Class2:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
       return "xxxx"


# c1 =Class2("马飞",99999999999999999)
# print(c1)   #打印这个类产生对象时候,会执行这个__str__(self),返回值只能是字符串类型




# 应用场景
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



#比如我们定义另外一个时间
class Date1(Data):
    pass
    def __str__(self):
        return 'xxxx1'


## 我们通过类的静态方法实例化的时候,发现d1的父类是Date并不是Date1,肯定不行
d1 = Date1.today()
print(d1)

##用classmethod改造
class Data3:
    def __init__(self,year,month,day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def today(cls):
        t = time.localtime()
        obj = cls(t.tm_year,t.tm_mon,t.tm_mday) ### 如何这样写,当Date1来调用这个方式相当于 obj=Date2(t.tm_year,t.tm_mon,t.tm_mday)来初始了
        return  obj


class Date4(Data3):
    pass
    def __str__(self):
        return 'xxxx1'

d2 = Date4.today()  #其实就等同于 d2 = Date4(xx,xx,xx) 很好理解
print(d2)


#静态方法  写死了的类方法,动态方法,灵活一些