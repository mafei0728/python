#!/usr/bin/env python
# -*- coding:utf8 -*-
# author:mafei0728

#property 属性

import math
class Circle1:
    def __init__(self,radius):
        self.radius = radius
    def area1(self):
        return math.pi * self.radius**2


    def perimeter1(self):
        return 2*math.pi*self.radius


c1 =Circle1(21)
print(c1.radius)
print(c1.area1())
print(c1.perimeter1())

## 对于圆形来说,确定了半径,圆的周长和面积都应该是确定的属性,需要使代码更加简洁.优雅
## 这个时候,我们用到property 入其名,属性

class Circle2:
    def __init__(self,radius):
        self.radius = radius

    @property  #类似装饰器,可调用的对象装饰可调用的对象 == area2 == property(area2)
    def area2(self):
        return math.pi * self.radius**2

    @property
    def perimeter2(self):
        return 2*math.pi*self.radius


c1 =Circle2(21)
print(c1.radius)
print(c1.area2)
print(c1.perimeter2)

## 这样调用,不用加括号,对于使用者,就是在调用对象的属性,并不知道里面是经过一系列计算得到的
## 1:访问方式统一
## 2:相当于封装,隐藏真实逻辑