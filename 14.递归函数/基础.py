#!/usr/bin/env python
# -*- coding:utf8 -*-
# author:mafei0728

###递归函数,函数的返回值是自己本身
def fun1(n):
    if n == 1:
        return 10
    if n > 1:
        return fun1(n-1) +2





print(fun1(4))


# 1:必须有一个明确的结束条件
# 2:每次进入一个更深的一层递归的时候,问题的规模比上次递归应该有所减少
# 3:递归效率不高,容易导致栈溢出 (在计算机中,函数的调用是通过栈(stack)这种数据结构来实现的,没进入一个函数的调用,就加一层栈
# 每当返回函数的时候,就会减少一层栈帧,由于栈的大小不是无限的,所以递归调用的次数超过最大,或者最大内存,就会导致栈溢出)


#python3 深默递归深度是1000
import sys
print(sys.getrecursionlimit())
##手动设置
sys.setrecursionlimit(1000)
print(sys.getrecursionlimit())