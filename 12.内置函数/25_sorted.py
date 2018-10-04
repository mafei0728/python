#!/usr/bin/env python
# -*- coding:utf8 -*-
# author:mafei0728

"""
    Return a new list containing all items from the iterable in ascending order.

    A custom key function can be supplied to customize the sort order, and the
    reverse flag can be set to request the result in descending order.
    """

#可迭代对象--到迭代器,next()后,放在列表里面排序
a={
    "a":1111111111,
    "b":222,
    "c":33332222,
    "d":333322,
}



#降序
print(sorted(a,reverse=True))
#按工资排序,自定义函数
print(sorted(a,key=lambda k:a[k]))
print(sorted(a,key=lambda k:a[k]))
#工资
res=zip(a.values(),a.keys())
c=dict(res)
print(sorted(c))