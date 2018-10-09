#!/usr/bin/env python
# -*- coding:utf8 -*-
# author:mafei0728

#通过字符串的形式来操作对象的相关属性,称为反射

class Class1:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def speak(self):
        print("%s在说话"% self.name)




c1 = Class1("mafei0728",18)
hasattr(c1,"name")  # 属性要用字符串来 本质通过 c1.__dict__来寻找,返回bool值

print(getattr(c1,"name"))  #获取属性

f1 = getattr(c1,"speak") #获取绑定方法

f2 = getattr(Class1,"speak") #获取类的函数
print(f1)
print(f2)
f1()
f2(c1)
#总结,类和对象操作方式一样,这种玩法就是反射
#当不确定,类的属性存在与否
print(getattr(c1,"test","获取不到的情况下返回我"))





#下面两个不常用
setattr(c1,"sex",21) # 设置
print(getattr(c1,'sex',1))
#删除
delattr(c1,'sex')
print(hasattr(c1,'sex'))

# python 一切皆对象,所以一切对象都可以用反射