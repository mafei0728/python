#!/usr/bin/env python
# -*- coding:utf-8 -*-

#自定义异常
class MafeiError(BaseException):
    def __init__(self,msg):
        self.msg = msg

    def __str__(self):
        return self.msg


try:
    raise MafeiError("okokok!!!")
except MafeiError as f:
    print(f)
x=1
y=1
## 断言,程序接下来的必须依赖一个条件往下走 类似linux if [ $? -eq 0 ]
assert x == y
print("ok")

# try和except替代 if逻辑,可以提升程序的健壮性和容错性,但是程序中尽量少用,异常处理是用来处理一些不可预料的错误
# 正常情况我们在逻辑层就该解决.可预知的异常