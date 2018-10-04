#!/usr/bin/env python
# -*- coding:utf8 -*-
# author:mafei0728


class Football_player:
    '''共同的属性'''
    sex='man'
    age='23'
    '''不同的属性,类实例化的时候指定'''
    def __init__(self,name,foot,strength):
        self.name1 = name
        self.foot1 = foot
        self.strength1 = strength
    '''共同的技能(函数)'''
    def kick_ball(self):
        print('%skick the ball '%(self.name1))

    def pass_ball(self,play):
        print('%s pass football to %s'%(self.name1,play.name1))


player1 = Football_player('mafei01','left',90)
player2 = Football_player('mafei02','left',94)
player3 = Football_player('mafei03','left',87)

#修改类属性
Football_player.coach = 'coach ma'

#修改实例属性
player1.high = '182'
player2.high = '194'
player3.high = '201'
player3.age = 25

#属性内存地址,同一种属性指向相同的地址节省资源
print(id(player1.age))
print(id(player1.age))

#不同的实例绑定方法内存地址不同
print(player1.kick_ball)
print(player2.kick_ball)

#查看类的namespace,类的字典无法操作
print(Football_player.__dict__)

#查看实例的namespace,实例的字典可以直接操作
print(player1.__dict__)
print(player2.__dict__)
print(player3.__dict__)

#总结:
## 1:实例化对象,有自己的命名空间.共有的属性不存在每个实例的命名空间里面,调用的时候从类中获取
## 2:类,增删查改影响,可能会影响所有实例化的对象的属性
## 3:实例化对象,的增删查改,只会影响自己
## 4:如果实例修改了类中的公有属性,则会存在自己的命名空间里面,但是不会影响其他实例化得对象
## 5.实例找属性,会先从自己的命名空间找,找不到,再去类里面找.类里面没有,就报错,不会去全局命名空间找,不是一个概念
## 6:所有的实例引用类变量,都指向一个内存地址,但是,由于实例化后,类的函数,在实例中是自己的绑定方法,所以每个实例的引用类同一个方法,的内存地址不用
## 7:类的变量尽量避免定义为可变类型