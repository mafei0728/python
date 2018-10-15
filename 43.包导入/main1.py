#!/usr/bin/env python
# -*- coding:utf-8 -*-


#包开发一系列功能给别人,不要单独去执行包里面的文件
#有__init__的文件夹是包
#凡是导入模块,有点且点的左边一定是一个包
#导入包的时候会执行包下面的__init__文件
import pagetest.test1.test11
#调用
pagetest.test1.test11.fun11()

#from导入
from pagetest.test2 import test21
test21.fun21()

#导入*
#导入包就是执行包下面的init文件,没有明确指定会报错
from pagetest.test1 import *
# 我们可以在包下面的__init__文件定义__all__
# __all__只会跟*匹配,跟导入模块一样
test11.fun11()

# 下面这种导入是常规导入方面,我们在__init__里面定义
# 里面定义绝对导入和相对导入
from pagetest import test2
test2.test21.fun21()


# 总结: 约定用import 导入内置模块和第三方模块,不要导入自定义的模块.
# 自定义的模块采用应该使用from ...import 的相对导入(尽量相对路劲,不要绝对)
# 对于包来说,相对导入只能用from的形式