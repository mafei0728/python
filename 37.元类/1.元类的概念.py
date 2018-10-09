#!/usr/bin/env python
# -*- coding:utf8 -*-
# author:mafei0728

#在解释元类之前,我们必须了解几个概念
# 1: python一切皆对象,类也是对象 所有的类都是type的类的对象
# 2:所有的类都继承object类

#一般情况下,我们产生类都是这样的
class Class2:
    x=1
    y=2



#但是本质上,是这样的,通过type产生的
class_name = 'Class'
class_dict = {     #不写也是默认的一些属性
    "x":1,
    "y":2
}
class_base = (object,)  #为空,这默认继承object

Class1 = type(class_name,class_base,class_dict)
# 发现我们手动定义的类,和通过type封装得到的类其实是一回事
print(Class1)
print(Class2)


