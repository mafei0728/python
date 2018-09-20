#!/usr/bin/env python
# -*- coding:utf8 -*-
# author:mafei0728
#带有yield关键字的函数,就是生成器
#生成器本质就是迭代器
from  collections.abc import Iterator
def fun():
    print('ok')
    yield 1 # return 1

# x = fun()
# print(isinstance(x,Iterator)) ##判断为迭代器
# print(next(x))

# 触发生成器,需要用next()方法,遇到yield停止,并返回一个值,再次next()就继续执行,直到报错
def fun2():
    for i in range(3):
        print(i)
        yield i
y = fun2()

# print(next(y))
# print(next(y))
# print(next(y))
# print(next(y))
# print(next(y))

#序列化了函数
for i in y:  ###等同于 next(y) 帮你解决超过报错的问题
    print(i)
#去玩就没有了
for i in y:
    print(i)
#跟return有明显的区别,return碰到函数就结束,只能返回一次值,yield碰到就停止,能返回多次值
#yield把函数变成生成器,生成器就是迭代器,具有next方法,序列化函数
#next()方法必须找到yield的值,不能就报错