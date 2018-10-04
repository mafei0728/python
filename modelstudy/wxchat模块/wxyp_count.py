#!/usr/bin/env python
# -*- coding:utf8 -*-
# author:mafei0728
import wxpy
bot = wxpy.Bot(cache_path=True)
my_friends = bot.friends()
#def sum_sex():
def sum_sex():
    '''统计女性'''
    sex_sum = {'男性': 0, '女性': 0, '无备注': 0}
    for friends in my_friends:
        if friends.sex == 1:
            sex_sum['男性'] += 1
        elif friends.sex == 2:
            sex_sum['女性'] += 1
        else:sex_sum['无备注'] +=1
    print(sex_sum)
    return sex_sum

def sum_pro(pro_sum):
   for friends in my_friends:
       if friends.province:
           if friends.province not in pro_sum:
                pro_sum[friends.province] = 0
           pro_sum[friends.province] += 1
   print(pro_sum)
   return pro_sum

a=sum_sex()
b=sum_pro(pro_sum={})
print(a,b,sep='\n')