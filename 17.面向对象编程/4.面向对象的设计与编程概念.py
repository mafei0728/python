#!/usr/bin/env python
# -*- coding:utf8 -*-
# author:mafei0728


# 我们定义一个中国足球男子u23的注册站点
# 首先我们要统计运动员共同的属性 性别,和年龄,是约束也是共同的属性
# 共同的方法,踢球和传球
# 还有每个运动员不同的身体条件
# 定义完了再去设计

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
# 运动员实例化其实就是执行Football.__init__(seft,xx,xx,xx)函数的过程
# 实例化就是实例化,属性和引用


# 总结
# 1:类属性 变量和函数
# 2:实例化 变量和绑定函数