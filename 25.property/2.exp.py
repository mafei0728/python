#!/usr/bin/env python
# -*- coding:utf8 -*-
# author:mafei0728


## BMI指数计算

class Person:
    def __init__(self,name,age,high,weight):
        self.name = name
        self.age = age
        self.high = high
        self.weight = weight

    @property
    def bodyindex(self):
        return self.weight/(self.high**2)



# p1 = Person('mafei',9999999999999999999,1.74,80)
# print(p1.bodyindex)


## 封装属性
class Person1:
    def __init__(self,name,money,age,address):
        self.__name = name
        self.__money = money
        self.__age = age
        self.__address = address

    @property
    def name(self):
        return self.__name

    #但是我们金钱是私有属性,但是经常在变化,我们改如何修改呢
    @property
    def money(self):
        return self.__money


    # 当被property装饰的对象,会有下面这个属性,可以修改私有属性
    @money.setter
    def money(self,values):
        if not isinstance(values,int):
            raise TypeError("必须是数字")
        self.__money = values

    @property
    def age(self):
        return self.__age

    @property
    def address(self):
        return self.__address

    @address.deleter   ##删除属性
    def address(self):
        del self.__address

# p = Person1('mafei0728',1000000000000000000,999999999999999999999999,"xx")
# print(p.age)
#
# p.list_money=9777777777777777777777777
# print(p.money)

##非数字会抛出异常
#p.money="1111"

#但是初始化时候不会,因为初始化时对应,self.__money=xxx,只有self.money=xx才会触发下面两个函数的执行

class Person2:
    def __init__(self, name, money, age, address):
        self.name = name
        self.money = money
        self.age = age
        self.address = address

    # @property
    # def list_name(self):
    #     return self.__name


    @property
    def money(self):
        return self.__money


    @money.setter
    def money(self, values):
        if not isinstance(values, int):
            raise TypeError("必须是数字")
        self.__money = values

    @money.deleter
    def money(self):
        del self.__money


    # @property
    # def list_age(self):
    #     return self.__age
    #
    # @property
    # def list_address(self):
    #     return self.__address
    #
    # @list_address.deleter  ##删除属性
    # def list_address(self):
    #     del self.__age


p = Person2('mafei0728', 1000000000000000000, 999999999999999999999999, "xx")

## 如果有用的 setter 其实不管初始化有没有用的__money,内部因为初始化self.money = xxx 会自动触发setter的执行,看上面
#他会把 xxx 传进去让 self.__money = money 封装起,如果传入字符串还是会报错,对传入值的限定
print(p.money) ##你调用这个,其实是调用那个函数
print(p._Person2__money) ##值已经被封装起来
# del p.money #调用删除的函数
# print(p.money)