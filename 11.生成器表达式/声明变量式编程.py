#!/usr/bin/env python
# -*- coding:utf8 -*-
# author:mafei0728

#这是一种声明变量式编程方法
y=(i for i in range(101))
#sum函数可以传入两个参数,1个可迭代对象,一个初始值,默认是0
a=sum(y)
print(a)

#求sum1z中商品总价格
with open('sum1') as f:
    '''split默认以空格,并去掉空字符串'''
    line1 = (int(line.split()[1]) * int(line.split()[2]) for line in f)
    print(sum(line1))

with open('sum1') as f:
    a=[{line.split()[0]:{int(line.split()[1]):int(line.split()[2])}} for line in f]
    print(a)
print(a[0]["a"])

with open('sum1') as f:
    a=(line.split() for line in f)
    c=({"name":i[0],'price':i[1],'num':i[2]} for i in a)
    print(next(c))

#取值大于xx
with open('sum1') as f:
    a=(line.split() for line in f)
    c=({"name":x,'price':float(y),'num':int(z)} for x,y,z in a if float(y)>3000)
    print(list(c))