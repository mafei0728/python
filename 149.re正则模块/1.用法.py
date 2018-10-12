#!/usr/bin/env python
# -*- coding:utf8 -*-
# author:mafei0728
import re
#用法1:
# 查找打所有匹配到的数据,范返回到一个列表里面
# re.findall()


# 只演示重点,容易忽视的问题
# 1:分组配置,优先级的问题
#re.findall(pattern, string, flags=0)
a = 'mamamatctab'
t1 = re.findall('(ma)+tct',a)  # 如果能成功,只会返回分组里面的
print(t1)

t2 = re.findall('(?:ma)+tct',a) # 正常匹配,取消分组匹配优先的特性.这两点都称为无命名分组
print(t2)
#分组匹配值在findall有效
#有命名的分组
card_id='429004198507293518'
c = re.search('(?P<province>\d{3})(?P<address>\d{3})(?P<birth>\d{8})(?P<id>\d{4})',card_id)
#可以通过key values来取值
print(c.group("id"))
print(c.groups())


#用法2:从开头开始匹配,如果没有成功 返回none,成功者返回一个对象
# re.match(pattern, string, flags=0)
a = re.match('aa','aassssaaa')
print(a)
print(a.group()) #取出


#用法3:从右向左匹配,找到第一个返回一个位置对象,
# re.search(pattern, string, flags=0)
b = re.search('aaa','hhhhaaaaafffaaaaaaaaaassdd')
print(b)
print(b.group())

#用法4 替换匹配
#re.sub(pattern, repl, string, count=0, flags=0)
a = 'sdsd111dfddf111'
print(re.sub('\d+',"",a,count=1))

# 还可以,将匹配的数字传入函数处理返回修改 将匹配的数字乘以 2
def double(matched):
    value = int(matched.group('value'))
    return str(value * 2)

s = 'A23G4HFD567'
print(re.sub('(?P<value>\d+)', double, s))

#同类用法,替换,并且和替换次数组成元祖返回
a = 'sdsd111dfddf111'
print(re.subn('\d+',"",a))



#用法5 查找,但是返回一个迭代器
#re.finditer(pattern, string, flags=0)
a = 'sdsd111dfddf121'
b = re.finditer('\d+',a)
print(b.__next__().group())
print(b.__next__().group())

#用法6,模糊匹配分割几次
c=re.split("\d+",'sdsds2323sdsd232sdsd232sdsd2323',2)
print(c)

#用法7.先编译规则,直接调用
res = re.compile('\d+')
c=res.findall('wewew23232j32j32j3232')
print(c)






#难点1:
#关于反斜杠,python中的普通反斜杠为\\,正则中的普通反斜杠也为\\,python如果要传给正则\\,需要\\\\,或者指定r,忽略python里面的转译
#这个例子应该很好理解
c = 'sdsd\dssd'
print(re.findall('d\\\\d',c))

#难点2
# \b在正则里面是边界匹配,在python里面是一个ascii里面有特殊意义
c= 'hello mafei0728'
print(re.findall(r'o\b',c))
print(re.findall(r'\bm',c))

#难点3
# 贪婪匹配,默认是贪狼匹配
# 非贪婪匹配,安最小匹配
print(re.findall("\d+","2232sdsds232ssds2323sdsdsd"))
print(re.findall("\d+?","2232sdsds232ssds2323sdsdsd"))










# 匹配网址
a = 'http://www.sdd.sdsds/ds@#/sdsd23/sds232sdws'
b = re.findall("https*://\w+\.\w+\..+",a)
print(b)


########################重点############################
#容易忘记混淆的几点,?指的是前一个字符0,1个ab?c  ac abc 不能匹配abbc
#[]号内元字符为普通符号,^为取反,-,\这三个有特殊意义
#.不能匹配\n
#空白字符用\s匹配 匹配任意空白字符，等价于 [\t\n\r\f]. \S取反
# http://www.runoob.com/python/python-reg-expressions.html