#!/usr/bin/env python
# -*- coding:utf8 -*-
# author:mafei0728
import json
pro_map = {
       "湖北":{
                "仙桃":{"张沟":["红光","红旗","胜利"],
                         "彭场":["中岭","陈豆","夏新"],
                         "毛嘴":["东湾",'沙岭','李滩']
                        },
                "洪湖":{"燕窝":['天门','洪丰','外坝'],
                         "新滩":['新洲','庙弯','八型'],
                         "峰口":['白庙','新台','全胜']
                        },
                "天门":{"多宝":['11','22','33'],
                         '拖市':['44','55','66'],
                         '小板':['77','88','99']
                        }
                },
       "四川":{

                },
       "湖南":{

                }
}

# 序列化,就是把一个对象变成可传输的对象,,对比字典保存在文件里面,通过网络传输到其他地方
# 反序列化则是相反的
# json是一个轻量级的数据交换格式


# 序列化
f = open('file1','w')
a = json.dumps(pro_map)
f.write(a)
f.close()
# 反序列化
f = open('file1','r')
b = json.loads(f.read())
f.close()
print(b)
print(type(b))

# 直接处理流,下面是处理句柄
f1 = open('file2','w')
json.dump(pro_map,f1)
f1.close()
f2 = open('file2','r')
c = json.load(f2)
print(c)
print(type(c))

# 惯性思维,不要以为序列化一定要写入文件和从文件读,也可以得到字符串,网络传输,等等

a=899999999999999
b="mafei0728"
c=[1,2,3,4]
d=(1,2,3,4)
e={"a":1,"b":2}
a = json.dumps(a)
b = json.dumps(b)
c = json.dumps(c)
d = json.dumps(d)
e = json.dumps(e)
print(a)
print(b)
print(c)
print(d)  #发现元组转成了列表的形式,其实他已经不是python的数据格式了
print(e)
print(type(json.loads(d)))

### json是轻量级数据交易工具,类似xml,等等其他玩意儿,都是做数据交换的

### json类型并不是只有字典形式包含,字典,字符串,列表,整数,浮点数,布尔(true/false),null