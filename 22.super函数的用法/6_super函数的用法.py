#!/usr/bin/env python
# -*- coding:utf8 -*-
# author:mafei0728


#定义传奇这个游戏
class Hero:
    life = 400
    defense = 30
    attack_value = 50
    level = 1
    step = 5
    def __init__(self,sex,name):
        self.sex = sex
        self.name = name
    def move(self):
        print("%s移动了%s步"%(self.name,self.step))

    def attack(self,play):
        play.life -= self.attack_value - play.defense

# 继承
class Warrior(Hero):
    '''基本剑术'''
    def __init__(self,sex,name,faction):
        #Hero.__init__(self,sex,name)
        #super(Warrior, self).__init__(sex, name) # <---------python2中的写法
        super().__init__(sex,name) # py3不需要写进去了.自动帮你解决继承的问题,按照继承的顺序,
        self.faction = '沙巴克'
    def attack(self,play):
        self.attack_value += 30
        super().attack(play)     # 派生的用法写可以这么写了
        self.attack_value -= 30
        print("%s还剩下%s血" % (play.name, play.life))

class Taoist(Hero):
    def summon(self):
        print("召唤神兽")

class Master(Hero):
    pass


w1 = Warrior('female','player1','沙巴克')
w2 = Warrior('female','player2','云霄阁')
w1.attack(w2)
w1.attack(w2)
w1.attack(w2)
w1.attack(w2)

## super()函数只能用于新式类,py2中必须将父类和self传递进去,py3就不需要了