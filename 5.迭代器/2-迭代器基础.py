#!/usr/bin/env python
# -*- coding:utf8 -*-
# author:mafei0728
#通过迭代器循环可迭代对象
a = [1,2,3,4,5,6]
b = iter(a)
# while True:
#     try:
#         print(next(b))
#     except StopIteration:
#         print('over')
#         break

for i in a:  #本质 a = a.__iter__()
    print(i)