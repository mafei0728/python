#!/usr/bin/env python
# -*- coding:utf8 -*-
# author:mafei0728

#定义学校
import time
class Teacher:
    def __init__(self,name,age,sex,course,date):
        self.name = name
        self.age = age
        self.sex = sex
        self.course = course
        self.date = date


class Student:
    def __init__(self,name,age,sex,course,teacher):
        self.name = name
        self.age = age
        self.sex = sex
        self.course = course
        self.teacher = teacher


class Course:
    def __init__(self, name, price, period):
        self.name = name
        self.price = price
        self.period = period

class Date:
    def __init__(self,date_time):
        self.date_time = date_time

d1 = Date(time.strftime('%F',time.localtime()))
c1 = Course('数学',15000,'1Y')
t1 = Teacher('Mir ma',53,'female',c1,d1)
s1 = Student('ma',9999,'male',c1,t1)
print(s1.course.name)
print(t1.date.date_time)
##组合,多个类组合在一起 关键字 xx要xx,实现代码的重用
