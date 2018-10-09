#!/usr/bin/env python
# -*- coding:utf8 -*-
# author:mafei0728

#可插拔编程
import test2
c1 = test2.Class("mafei0728")
print(c1)

#假设我们test2中的功能没有写完,我们希望test1中能够继续写下去

if hasattr(c1,"fun1"):
    f1 = getattr(c1,"fun1")
    f1()
else:
    pass


#这样不会影响我test1的整体逻辑,等test2中功能写完,也能正常运行了