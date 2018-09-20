#!/usr/bin/env python
# -*- coding:utf8 -*-
# author:mafei0728
import time
def fun1(login='file'):
    def fun2(fun):
        def fun3(*args,**kwargs):
            if login == 'file':
                start_time = time.time()
                with open('current_login','r+') as f,\
                     open('lock','r+') as g,\
                     open('user_passwd','r') as h:
                     a = eval(f.read())
                     b = eval(g.read())
                     c = eval(h.read())
                if a['name'] and a['login_status'] and b['status']:
                    res = fun()
                    return res
                while True:
                    count = 0
                    user = input('user:')
                    passwd = input('passwd:')
                    if c['user'] == user and c['passwd'] == passwd:
                        res = fun()
                        return res
                    else:
                        count += 1
                        if count == 3:
                            current_time =time.time()
                            a['time'] = current_time
                            a['user'] = user
                            a['status'] = True
            
                    stop_time = time.time()
                    print('time run is %s'%(stop_time-start_time))
        return fun3


    return fun2




@fun1()
def fun():
    time.sleep(3)
    print('welcome to china')
    return 0