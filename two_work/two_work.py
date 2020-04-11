#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""第二天作业"""



def test(info):
    if info["username"] == 'root' and info['passwd'] == '123':
        print('你有权限')
    else:
        print('你没有权限')
        return
    data = "1,2,3"
    return data


def test2(info):
    if info["username"] == 'root' and info['passwd'] == '123':
        print('你有权限')
    else:
        print('你没有权限')
        return
    data2 = "4,5,6"
    return data2

def permit(func):
    def verify(info):
        func(info)
    return verify


@permit
def test2(info):
    data2 = "4,5,6"
    return data2

# test({'username':'root', 'passwd':'123'})

@permit
def test(info):
    data = "123"
    return data


# 实现permit装饰器对权限进行验证

'''
2.
递归函数列出所有文件
使用os.listdir
os.isfile
练习找出单个目录中的最大文件
练习找出目录树中的最大文件
'''
import os

def all_dir(path):
    for file in os.listdir(path):
        pa = os.path.join(path, file)
        if not os.path.isdir(pa):
            print(pa)
        else:
            all_dir(pa)

# all_dir('F:\\testops product16\one day\\test')

def max_size(path):
    sizelist = []
    for file in os.listdir(path):
        pa = os.path.join(path, file)
        if not os.path.isdir(pa):
            sizelist.append(os.path.getsize(pa))
            return sizelist
        else:
            max_size(pa)
if __name__ == '__main__':
    if max(max_size('F:\start\Cross')):
        print(max(max_size('F:\start\Cross')))

