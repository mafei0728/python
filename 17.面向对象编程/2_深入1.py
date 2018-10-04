#!/usr/bin/env python
# -*- coding:utf8 -*-
# author:mafei0728

#创建一个男子U23奥运足球运动员的类
class Football_player:
    '''共同的属性'''
    sex='man'
    age='23'
    '''不同的属性,类实例化的时候指定'''
    def __init__(self,name,foot,strength):
        self.name1 = name
        self.foot1 = foot
        self.strength1 = strength
        self.tech=[]
    '''共同的技能(函数)'''
    def kick_ball(self):
        print('%skick the ball '%(self.name1))

    def pass_ball(self,play):
        print('%s pass football to %s'%(self.name1,play.name1))


player1 = Football_player('mafei01','left',90)
player2 = Football_player('mafei02','left',94)
player3 = Football_player('mafei03','left',87)

print(player1.name1) # <-----------调用类的变量,绑定变量
print(player1.foot1)
player1.kick_ball() # <------------调用类的方法,这里称为绑定方法
Football_player.kick_ball(player1) #<--------等同于上面
player1.pass_ball(player2) # 还能穿一个对象进去交互,看你怎么定义类的函数了


# 总结
## 1: 类可以实例化得到对象,可以通过类.变量名,类.函数名(对象) 来引用
## 2: 实例即对象,引用名字 通过实例名.类的变量,实例名.绑定方法,实例名.自己的变量名来调用