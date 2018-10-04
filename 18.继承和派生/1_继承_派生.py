#!/usr/bin/env python
# -*- coding:utf8 -*-
# author:mafei0728

## python支持多继承.用逗号分开
## 1:解决代码的重用性
class Class1:
    pass

class Class2:
    pass

class Class3(Class1):
    pass

class Class4(Class1,Class2):
    pass


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
        Hero.__init__(self,sex,name)  #<----如果子类有父类不同的属性称为派生
        self.faction = '沙巴克'        #<----如果子类有父类不同的属性称为派生
    def attack(self,play):
        self.attack_value += 50
        Hero.attack(self,play)
        self.attack_value -= 50
        print("%s还剩下%s血"%(play.name,play.life))


class Taoist(Hero):
    def summon(self):
        print("召唤神兽")  # <-----派生,父类没有的,或者重名的属性

class Master(Hero):
    pass
w1 = Warrior('female','player1','沙巴克')
w2 = Warrior('female','player2','云霄阁')
w1.attack(w2)
w1.attack(w2)
w1.attack(w2)
w1.attack(w2)

## 通过继承来实现代码重用,通过派生来实现,独有的属性 关键字xx是xx