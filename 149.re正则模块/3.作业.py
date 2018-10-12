#!/usr/bin/env python
# -*- coding:utf-8 -*-
import re
a = "(3*( 4+ 50 )-(( 100 + 40 )*5/2- 3*2* 2/4+9)*((( 3 + 4)-4)-4))"
def fun1(k):
    if re.search('\s*',k):
        k = re.sub("\s*","",k)

    gg = re.findall(r'[()+\-*/]',k)
    if gg and len(gg)>1:
        k = re.sub(r'\([^()]*\)',sum_fun,k)
        return fun1(k)
    return k

def  sum_fun(Match):
    if not isinstance(Match,str):
        Match = Match.group()
        Match = re.search("-?\d.*\d",Match)
        Match = Match.group()
    Match = Match.replace('--','+')
    Match = Match.replace('-+', '-')
    if "*" in Match:
        Match = re.sub(r'\d*\.?\d*\*-?\d*\.?\d*',mul,Match,count=1)
        return sum_fun(Match)
    if "/" in Match:
        Match = re.sub(r'\d*\.?\d*/-?\d*\.?\d*',div,Match,count=1)
        return sum_fun(Match)
    if re.search('^-?\d*\.?\d*\+',Match):
        Match = re.sub(r'^-?\d*\.?\d*\+-?\d*\.?\d*',add,Match,count=1)
        return sum_fun(Match)
    if re.search('^-?\d+\.?\d*-',Match):
        Match = re.sub(r'^-?\d*\.?\d*--?\d*\.?\d*',subt,Match,count=1)
        return sum_fun(Match)
    return Match
def mul(exp):
    exp=exp.group()
    g = re.split(r'\*+', exp)
    return str(float(g[0]) * float(g[1]))

def div(exp):
    exp = exp.group()
    g = re.split(r'/+', exp)
    return str(float(g[0]) / float(g[1]))

def add(exp):
    exp = exp.group()
    g = re.split('\++', exp)
    return str(float(g[0]) + float(g[1]))

def subt(exp):
    exp = exp.group()
    g = re.split('-',exp)
    return str(float(g[0]) - float(g[1]))


b=fun1(a)
print(b)
print(eval(a))