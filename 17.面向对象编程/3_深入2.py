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

# 类的增删查改,会影响到所有的对象
Football_player.coach = 'coach ma'
del Football_player.coach
Football_player.age = 24


player1 = Football_player('mafei01','left',90)
player2 = Football_player('mafei02','left',94)
player3 = Football_player('mafei03','left',87)

#对象的增删查改,只会影响自己
player1.coach = 'coach liu'
player1.age = 25
del player1.coach
