#!/usr/bin/env python
# -*- coding:utf8 -*-
# author:mafei0728
import random

#0到的浮点型数字,无边界
print(random.random())



#取a,b之间的整数,包含边界
print(random.randint(-1,10))


#取a,b之间的数,包含左边界
print(random.randrange(-1,1))


#在序列里面选1个元素,类型为元素的类型
print(random.choice(range(2)))


#从可迭代对象取一个放在列表里面
print(random.choices([1,2,3,4,5]))


#从序列里面选n个放在列表里面
print(random.sample(range(4),2))


#去范围任意小数
print(random.uniform(1,2))


#洗牌,没有返回值
c = list(range(10))
print(c)
random.shuffle(c)
print(c)

#####################总结,上面设计的序列,就是包含可迭代对象,比如字符串
#验证码
def check_five(x:int):
    ver_code = ''
    for i in range(x):
        n1 = str(random.randint(0,9))
        n2 = chr(random.randint(65,90))
        n3 = chr(random.randint(97,122))
        cod =random.choice([n1,n2,n3])
        ver_code += cod
    return ver_code
print(check_five(7))

#写法2
import string
def check_code(x):
    a = string.ascii_letters+string.digits
    b = "".join(random.sample(a,x))
    return b
print(check_code(11))