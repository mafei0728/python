#!/usr/bin/env python
# -*- coding:utf8 -*-
# author:mafei0728
#匿名函数的一些思考

#1:比如有这样一个问题
a = [lambda x:x*i for i in range(5)]
print(a)
for b in a:
    print(b(2))


#2:其实可以拆开了解
def fun1():
    for d in range(5):
        pass
    e=lambda x:x*d
    return e
f1 = fun1()
print(f1(4))


#3:再来分析一下lambda接受值的问题

f = lambda x,y:x+y
#需要传递2个值,我么来分析下过程.运行函数的时候,结果为x+y,需要在作用域来引用x,y的值,少一个则报错,你只要不加括号运行,函数本身只是存在内存中

#4 在回过头来分析
a = [lambda x,y:x*y for y in range(5)]
print(a)
for b in a:
    print(b(2))
#明显会报错,因为少一个位置参数,因为,列表生成器.里面只是生成了5个函数,有的不懂,以为会把y值要传进去,假如是传进去运行了,看3点,肯定会报错,因为我们有2个参数,你传一个是不是会报错,所以没有假如

#上面的写法 无异于下面写法,不要被前后两个相同的值搞混了,只不过在列表里面存了5个一样的函数而已,列表中每一个元素都指向不同内存地址
a = [lambda x,y:x*y for k in range(5)]
print(a)
for b in a:
    print(b(2,2))

# 5 还有疑问,z1和z2的区别
z1 = [lambda x, y: x * y for y in range(10)]
z2 = [lambda x, y=y: x * y for y in range(10)]


# 还是分开写
# z1
def fun3():
    k = []
    for y in range(10):
        def fun3(x, y):  #本质上y只是定义了形参,并没有y=x的传参的动作
            return x * y

        g = fun3
        k.append(g)
    return k


for gg in fun3():
    print(gg(2))  #所以会报错少1个位置参数


# z2
def fun4():
    k = []
    for y in range(10):
        def fun4(x, y=y): #有传参的动作,定义默认参数,定义的时候y会在作用域找,
            return x * y

        g = fun4
        k.append(g)
    return k


for gg in fun4():
    print(gg(2))