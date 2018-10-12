#!/usr/bin/env python
# -*- coding:utf-8 -*-

#异常指程序运行过程中跑出的错误信息
#异常处理就是捕捉异常,进行处理,避免程序退出

# 1:捕捉,处理
try:
    print(x)
except NameError as f:
    print(f)
    x =1
    print(x)


#2: 多分子的捕捉处理
dict1 = {
    "x":1,
    "y":2,
}
try:
    print(dict1["z"])
except NameError as f1:
    print(f1)
except KeyError as f2:
    print(f2)
    dict1["z"]=2
    print(dict1["z"])


#3:当多种异常只需要一种处理方式的时候,我们可以,用下面的方法,语法错误不行


try:
    print(x1)
except Exception as f3:
    print(f3)

#4 混合使用,这种用的多

dict2 = {
    "x":1,
    "y":2,
}
try:
    print(dict2["xxx"])
except NameError as f1:
    print(f1)
except IndexError as f2:
    print(f2)
    dict1["z"]=2
    print(dict1["z"])
except Exception as f4:
    print(f4)

#5 异常最后处理

dict2 = {
    "x":1,
    "y":2,
}
try:
    print(dict2["xxx"])
except NameError as f1:
    print(f1)
except IndexError as f2:
    print(f2)
    dict1["z"]=2
    print(dict2["z"])
except KeyError as f9:
    dict2["xxx"] = 7
    print(dict2["xxx"])
    print(f9)
except Exception as f4:
    print(f4)
else:
    print("代码没有异常,才会执行此步骤")
finally:
    print("这是清理操作,物理代码是否异常,都执行")