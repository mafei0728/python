#!/usr/bin/env python
# -*- coding:utf8 -*-
# author:mafei0728
import json

#接上一个用法来讲
### json类型并不是只有字典形式包含,字典,字符串,列表,整数,浮点数,布尔(true/false),null
##我们在file3手动定义写一些json数据类型
f = open("file3",'r')
for i in f:
    c = json.loads(i)
    print(type(c))

#发现可以直接loads,只要符合json格式都可以直接loads

#注意几点,json 格式只能双引号,不能是元组反序列化,元组序列后直接成列表

#json可以与其他文件交换数据,但是很多数据类型不支持

#一个文件处理一个数据,多个数据处理成一个字典对象