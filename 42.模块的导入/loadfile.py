#!/usr/bin/env python
# -*- coding:utf-8 -*-


#fa

import testmodel1


print(testmodel1.name1)
c1 = testmodel1.Class1()
print(c1.id)

#反射也是可以用的
getattr(testmodel1,'fun1')()


#查看当前导入的模块
import sys
print(sys.modules)