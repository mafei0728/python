#!/usr/bin/env python
# -*- coding:utf8 -*-
# author:mafei0728

## python没有接口这个概念,接口 指用一堆函数来实现一堆方法
# 在python只能用继承来模拟接口

### 父类只负责定义'接口',子类来实现,称为归一化设计,用起来更统计,,类似linux中一切皆文件
class Animal1:
    def run(self):
        raise AttributeError("必须实现")    #<----限定之类必须实现,否则报错

    def speak(self):
        raise AttributeError("必须实现")    #<----限定之类必须实现,否则报错

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

p1 = People1()
P1 =Pig1()
#调用方法一样,但是现实的过程不一样
p1.run()
P1.run()

#抽象类来实现,正常的用来限制子类必须实现父类加了装饰器的方法
import abc

class Animal2(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def run(self):
        pass
    @abc.abstractmethod
    def speak(self):
        pass

class People2(Animal2):
    # def run(self):
    #     print('人正在跑')
    #
    # def speak(self):
    #     print('人正在说话')
    pass


class Pig2(Animal2):
    def run(self):
        print('猪正在跑')

    def speak(self):
        print('猪正在说话')

p2 = People2()


### 父类只负责定义'接口',子类来实现,称为归一化设计,用起来更统计,,类似linux中一切皆文件
### 用第三方的模块实现接口zope.interface