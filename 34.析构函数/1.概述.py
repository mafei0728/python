#!/usr/bin/env python
# -*- coding:utf8 -*-
# author:mafei0728
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

    def __getattr__(self, item):
        return getattr(self.h,item)

    def __del__(self): #程序退出,或者对象被删除,执行析构函数,立即回收
        self.h.close()
        print("game over!!!")
f2 = Open1("test2")

f2.write("mafei0728")
f2.write("mafei0728")
f2.write("mafei0728")
f2.write("mafei0728")
f2.write("mafei0728")
f2.seek(0)
print(f2.read())
print(f2.__dict__)
