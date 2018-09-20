#!/usr/bin/env python
# -*- coding:utf8 -*-
# author:mafei0728
#判断对象是否是迭代器和迭代对象
from collections.abc import Iterable,Iterator
a = [1,2,3,4,5,6]
b = iter(a)
print(isinstance(a,Iterable))
print(isinstance(b,Iterator))