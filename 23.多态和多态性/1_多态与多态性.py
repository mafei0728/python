#!/usr/bin/env python
# -*- coding:utf8 -*-
# author:mafei0728

## 同一种类的不同形态,称为多态(定义角度)
import abc

class Animal1(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def run(self):
        raise AttributeError("必须实现")
    @abc.abstractmethod
    def speak(self):
        raise AttributeError("必须实现")

class People1(Animal1):
    def run(self):
        print('人正在跑')

    def speak(self):
        print('人正在说话')


class Pig1(Animal1):
    def run(self):
        print('猪正在跑')

    def speak(self):
        print('猪正在说话')

s1 = People1()
s2 = Pig1()
s1.run()
s2.run()

def fun1(object):  # 将这种调用方式,统一成一种调用的方式,产出不同的结果,称为多态性(使用者角度)
    object.run()
# 人和猪都是不同动物的多种形态的
# 调用的方法一样,传入不同类型的值(对于类型没有限制),逻辑一样,但是执行结果不一样
# 比如我们sum(),len(),等函数的时候,我们传入不同可迭代的数据类型,都能得到结果,这就是多态性,python如果说的不严谨,就是天生支持多态
# 多态使程序更加灵活
# 增加了程序的可扩展性