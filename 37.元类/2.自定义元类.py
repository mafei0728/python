#!/usr/bin/env python
# -*- coding:utf8 -*-
# author:mafei0728

#一般情况下,我们定义类的时候,元类都默认是type,现在我们自定义一个元类,让通过这个元类产生类的函数的,注释不能为空,类的注释也不能为空
#通过元类定义类的的时候.会执行元类里面的__init__函数
class Meta_lass(type):
    def __init__(self,class_name,class_bases,class_dict):
        self.class_name = class_name
        self.class_base = class_bases
        self.class_dict = class_dict
        if not self.__doc__:
            raise TypeError("类必须写注释")

        for class_value in class_dict:
            if not callable(class_dict[class_value]):continue
            if not class_dict[class_value].__doc__:
                raise TypeError("函数必须写注释")

class Class(metaclass=Meta_lass):
    '''xxx'''
    x=2
    def fun1(self):
        '''xx'''
        print("xxx")

