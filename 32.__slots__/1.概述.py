#!/usr/bin/env python
# -*- coding:utf8 -*-
# author:mafei0728

# 取消对象的命名空间,且规定对象的属性只能是slots包含的字符串元素名字的属性,节省了内存,限制你对象的属性
class Class:
    __slots__ = ["name","age"]
    sex = "female" # 不能限制类的
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def talk(self):   # 不能限制类的
        print("xxx")

c1 = Class("mafei0728",11)
print(c1.name)
print(c1.age)
print(c1.sex)
c1.talk()
#print(c1.__dict__)
#c1.sex = 'female'