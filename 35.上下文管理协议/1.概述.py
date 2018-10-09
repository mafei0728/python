#!/usr/bin/env python
# -*- coding:utf8 -*-
# author:mafei0728

#深度解析with open 为什么会自动关闭

with open("test","w") as f:
    f.write("mafei0728")





class Class:
    def __enter__(self):
        return self  #<--------------返回给对象


    def __exit__(self, exc_type, exc_val, exc_tb):
        print(exc_type)
        print(exc_val)
        print(exc_tb)
        return True  # <---------------处理异常,是程序不会报错,正常退出,后面的代码不会执行



with Class() as obj:  # as 会触发类里面的__enter__函数
    print("----------->",obj)
    raise TypeError("xxxx") #异常或者结束触发 __exit__函数
    print("wo shi xxxx")
print("wo shi xxx")