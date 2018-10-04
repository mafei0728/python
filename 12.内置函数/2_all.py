#!/usr/bin/env python
# -*- coding:utf8 -*-
# author:mafei0728

"""
 Return True if bool(x) is True for all values x in the iterable.

 If the iterable is empty, return True.
 """

###穿一个可迭代对象,如果所有元素全部为true,返回为True
print(all([1,2,3,4]))
print(all([]))
print(all([1,0]))
print(all(''))
print(all(' '))