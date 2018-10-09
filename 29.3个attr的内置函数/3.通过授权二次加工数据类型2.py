#!/usr/bin/env python
# -*- coding:utf8 -*-
# author:mafei0728

#我们现在的需求是没写一行,行头加上时间
import time

# class Open:
#     def __init__(self,filepath,mode="w",encode="utf8"):
#         self.h = open(filepath,mode=mode,encoding=encode)
#         self.filepath = filepath
#         self.mode = mode
#         self.encode = encode
#
#     def write(self,line):
#         current_time = time.strftime("%F %X")
#         self.h.write("%s %s%s"%(current_time,line,"\n"))


# f = Open("test")
# f.write("mafei0728")
# f.write("mafei0728")
# f.write("mafei0728")
# f.write("mafei0728")
# f.write("mafei0728")

#但是上面我们遇到了一个问题,如果我们要用文件句柄的其他时候,我们必须要操作f.h.xxx,这里又没有上面的继承,所以就要用到__getattr__

import time

class Open1:
    def __init__(self,filepath,mode="w+",encode="utf8"):
        self.h = open(filepath,mode=mode,encoding=encode)
        self.filepath = filepath
        self.mode = mode
        self.encode = encode

    def write(self,line):
        current_time = time.strftime("%F %X")
        self.h.write("%s %s%s"%(current_time,line,"\n"))

    def __getattr__(self, item):  # 当没有的时候我么执行这一步
        return getattr(self.h,item)  # 当找不到这个方法的时候,执行有这种方法的方法的内存地址给对象,__getattr__终极操作

f2 = Open1("test2")

f2.write("mafei0728")
f2.write("mafei0728")
f2.write("mafei0728")
f2.write("mafei0728")
f2.write("mafei0728")
f2.seek(0)
print(f2.read())
print(f2.__dict__)

# 总结:也就是说,当我们,无法使用继承来定制功能的时候,通过函数,比如像文件句柄,我们可以定义一个类,来派生新方法,为了不影响其他的方法,我们通过 __getattr__转一下