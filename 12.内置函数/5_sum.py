#!/usr/bin/env python
# -*- coding:utf8 -*-
# author:mafei0728

"""
    Return the sum of a 'start' value (default: 0) plus an iterable of numbers

    When the iterable is empty, return the start value.
    This function is intended specifically for use with numeric values and may
    reject non-numeric types.
    """

#传入可迭代 求和
v=sum(i for i in range(10))
print(v)