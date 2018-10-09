#!/usr/bin/env python
# -*- coding:utf8 -*-
# author:mafei0728


# 通过上下文管理协议实现with open

import time

class Open1:
    def __init__(self,filepath,mode="w+",encode="utf8"):
        self.h = open(filepath,mode=mode,encoding=encode)
        self.filepath = filepath
        self.mode = mode
        self.encode = encode

    def __enter__(self):  #<=================定义开始
        return self


    def write(self,line):
        current_time = time.strftime("%F %X")
        self.h.write("%s %s%s"%(current_time,line,"\n"))

    def __getattr__(self, item):
        return getattr(self.h,item)

    def __exit__(self, exc_type, exc_val, exc_tb):  # <=================定义结束
        self.h.close()
        print(exc_type)
        print(exc_val)
        print(exc_tb)
        print("---------------------------")

with Open1("test2") as f2:
    f2.write("mafei0728")
    f2.write("mafei0728")
    f2.write("mafei0728")
    f2.write("mafei0728")
    f2.write("mafei0728")
    f2.seek(0)
    print(f2.read())
    print(f2.__dict__)
