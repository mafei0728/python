#!/usr/bin/env python
# -*- coding:utf8 -*-
# author:mafei0728
#类
# 1:一系列对象用户共同的属性和特性抽象为类
# 2:类实例化得到具体的对象
# 3.类名,约定首字母大写

class Daoshi:
    #属性
    x = 1
    y = 'x'
    #方法
    def fun1(self):
        print("XX")

#应用类的特征(类的变量)和技能(类的函数)
print(Daoshi.x)
Daoshi.fun1(111) #<----要传入一个对象




#实例化得到对象,批量生产,他们有共同的属性(同一个类的变量)和技能(同一个类的函数)
dashi1=Daoshi()
dashi2=Daoshi()
dashi3=Daoshi()
dashi4=Daoshi()
dashi5=Daoshi()
#使用方法和属性
print(dashi1.x)
dashi1.fun1()


