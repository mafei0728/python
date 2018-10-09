#!/usr/bin/env python
# -*- coding:utf8 -*-
# author:mafei0728
import test


#反射模块的属性
c1 = getattr(test,'Class')
print(type(c1))

t1=getattr(test,"fun1")
t1()