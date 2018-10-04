#!/usr/bin/env python
# -*- coding:utf8 -*-
# author:mafei0728


class Wow:
    __skill='笑'
    def __init__(self,life_values,attack_values): #人物的生命值,我不希望直接被人调用,修改
        self.__life_values=life_values  #  _Wow__life_values
        self.__attack_values=attack_values # _Wow__attack_values
    def list_life(self):
            print(self.__life_values)  #在内部可以直接调用,外部不行,外部要用,可以写这种接口

    def attacked(self,enemy):
            self.__life_values = self.__life_values - enemy.__attack_values
            print("我被攻击了,还剩下%s"%(self.__life_values - enemy.__attack_values))

w1=Wow(200,20) # ---一旦初始化,生命和攻击外部将无法修改
w2=Wow(300,50)
w2.attacked(w1)
w2.__life_values =1000 #改了也没用.因为在定义前,__life_values == _Wow__life_values,定以后更改无用,你修改只不过子类自己加了个另外一个属性
w2.attacked(w1)
w2.attacked(w1)
w1.list_life()

class A:
    def __fun1(self): # 定义阶段转为_A__fun1
        print("A")
    def test(self):
        self.__fun1() # self._A_fun1

class B(A):
    def __fun1(self): # _B__fun1
        print("B")


b1=B()
b1.test()
#所以通过上面的注释可以知道,运行结果为A,类的私有属性,无法被子类继承和覆盖
#随便想想也知道,我游戏的攻击和生命,随便被子类或者外面更改 怎么玩?