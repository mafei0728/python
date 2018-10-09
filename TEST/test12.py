#!/usr/bin/env python
# -*- coding:utf8 -*-
# author:mafei0728
#
# f1 = [lambda x:x*i for i in range(5)]
# print(type(f1))
# print(f1[0](2))
#
# #引用变量的个数
# print(f1[0].__closure__)
# #取出来
# print(f1[0].__closure__[0].cell_contents)
# # print("-----------------")
# # def fun():
# #     for f2 in f1:
# #         print(f2(2))

#
#
# def fun1():
#     tem = [lambda x,i=i:x*i for i in range(5)]
#     return tem
#
#
# f1 =fun1()
# y = f1[0](2)
# print(y)
# for i in f1:
#     print(i(2))
#
# tem = [lambda x,i=i:x*i for i in range(5)]
#
# for i in tem:
#     print(i(2))

#
# a= [lambda x,i:x*i for i in range(5) ]
# print(a[0](1))


