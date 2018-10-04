#!/usr/bin/env python
# -*- coding:utf8 -*-
# author:mafei0728
import time

class Student:
    def __init__(self,id_cart,name,age):
        '''student'''
        self.id_cart = id_cart
        self.name = name
        self.age = age
        self.course = []
        self.check_in=[]
        '''0,1,2'''
        self.pay=0

    def study(self):
        '''考勤'''
        self.check_in.append(time.strftime('%F %X'))
        print('%s to go class'%self.name)

    def choice_course(self,course):
        '''选课'''
        self.course.append(course)

    def pat(self,status):
        '''缴费'''
        self.pay=status

class Classroom:
    company = '厦门大学'
    tel = ''
    admin = '黄老师'
    def __init__(self,address,name,classroom_stu):
        self.address = address
        self.name = name
        self.classroom_stu = classroom_stu
        self.time_reg =['forenoon','afternoon','evening']
    def register(self,unm_peo):
        self.classroom_stu -= unm_peo
        print('注册')

class Course:
        def __init__(self,name,teacher):
            self.name = name
            self.teacher = teacher
