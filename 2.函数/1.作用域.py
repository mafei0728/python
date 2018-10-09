#!/usr/bin/env python
# -*- coding:utf8 -*-
# author:mafei0728

#全局
print(globals())
#局部
print(locals())


#局比和内置
print(dir(globals()))
print(dir(locals()))
#内置方法和函数
print(dir(__builtins__))