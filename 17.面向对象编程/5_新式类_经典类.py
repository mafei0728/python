#!/usr/bin/env python
# -*- coding:utf8 -*-
# author:mafei0728

#python3没有区别,全是新式类

class Dclass:
    pass

#python2 ,新式类按下面的写法
class Aclass(object):
    pass

class Bclass(Aclass):
        pass

# 查看父类或者基类
print(Aclass.__bases__)
print(Bclass.__bases__)
print(Dclass.__bases__)


#总结py3默认基类object,继承了object的类都称为新式类,py2中新式类必须要括号写出object
#py2中不写括号写出object,则称为经典类