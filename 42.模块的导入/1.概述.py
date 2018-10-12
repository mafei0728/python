#!/usr/bin/env python
# -*- coding:utf-8 -*-

#1.模块分为三类,自定义,第三方和内建模块

#2.导入模块 1.创建名称空间;2.执行导入模块内可执行的语句;3.创建模块名,指向刚才创建的名称空间

#几种导入方式

import sys
sys.path

import  os as s #别名
#s.replace()
#s.open()


from testmodel1 import fun1,name1
# 重点1:
#直接可以赢,相当于把代码复制到本地,有弊端,容易出现同名覆盖
#但是fun1的局部作用域还是在他本身的模块
print(name1)
name1='sssss'
print(name1)
#这个回去他直接的作用域去寻找
fun1()
#如果当前的位置有冲突,可以取别名
from testmodel1 import fun1 as localf1

localf1()

# 重点2:
#导入所有,不建议,会冲突,
from testmodel1 import *
#可以在模块中用下面来控制*的导入,只能导入列表里面的
__all__=['name1','fun1']

# 重点3:
# python的模块不支持重载


bn
# 重点4:我们模块的测试通常会这么做
if __name__ == "__main__":
    print("xx")



# 重点5: 模块搜索路径 内存(sys.module)---内建----path (sys.path)
print(sys.path)


# 重点6:导入模块的时候,会在被导入模块的路劲生产一个编译的文件,可以通过一些参数先编译产生模块的缓存的文件