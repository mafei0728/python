#!/usr/bin/env python
# -*- coding:utf8 -*-
# author:mafei0728

"""
map(func, *iterables) --> map object

Make an iterator that computes the function using arguments from
each of the iterables.  Stops when the shortest iterable is exhausted.
"""

###  map
a=[1,2,3,4,5,6]
c=map(lambda x:x**2,a)
print(list(c))

"""
reduce(function, sequence[, initial]) -> value

Apply a function of two arguments cumulatively to the items of a sequence,
from left to right, so as to reduce the sequence to a single value.
For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates
((((1+2)+3)+4)+5).  If initial is present, it is placed before the items
of the sequence in the calculation, and serves as a default when the
sequence is empty.
"""

from functools import reduce
### reduce
a=range(100)
print(reduce(lambda x,y:x+y,a))



"""
    filter(function or None, iterable) --> filter object

    Return an iterator yielding those items of iterable for which function(item)
    is true. If function is None, return the items that are true.
    """

a={
    "a":1111111111,
    "b":222,
    "c":33332222,
    "d":333322,
}

### filter

c=filter(lambda x:a[x]==222,a)
print(next(c))
