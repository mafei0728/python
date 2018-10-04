#!/usr/bin/env python
# -*- coding:utf8 -*-
# author:mafei0728
a=('name%s'%i for i in range(20))
print(a)
#类型转换,迭代器可以转换成列表
b = list(a)
print(b)

