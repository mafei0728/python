#!/usr/bin/env python
# -*- coding:utf8 -*-
# author:mafei0728

class Class1:
    pass



class Class2(Class1):
    pass


# 判断子类
print(issubclass(Class2,Class1))

#类似__base__

print(Class1.__bases__)
print(Class2.__bases__)