#!/usr/bin/env python
# -*- coding:utf8 -*-
# author:mafei0728
def search_object():
    print('查找')

def delete_object():
    print('删除')

def add_object():
    print('增加')

def change_object():
    print('修改')

cmd_dict = {
    'search':search_object,
    'delete':delete_object,
    'add':add_object,
    'change':change_object
}

def tell_msn():
    msn = '''
    1.查找
    2.删除
    3.增加
    4.修改
    '''
    print(msn)


if __name__=='__main__':
    while True:
        tell_msn()
        choice_t = input("what are your want to do:")
        choice_t = int(choice_t)
        if choice_t == 1:
            cmd_dict['search']()
        if choice_t == 2:
            cmd_dict['delete']()
        if choice_t == 3:
            cmd_dict['add']()
        if choice_t == 4:
            cmd_dict['change']()
