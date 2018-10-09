#!/usr/bin/env python
# -*- coding:utf8 -*-
# author:mafei0728
#我们我们接收外外部输入的模块,通过下面的方法导入
#方法一 (不推荐)
m = input("-->")
m1 = __import__(m)
print(m1)

#方法二 推荐
import importlib

t1 = importlib.import_module(m)
print(t1)