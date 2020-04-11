#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""bytes 序列化与反序列化"""
import pickle
l = [1,2,3,4,]
dum = pickle.dumps(l)
# print(dum)

loa = pickle.loads(dum)
# print(loa)

"""序列化类"""

class Record:
    def __init__(self, name):
        self.name = name

obj_dum = pickle.dumps(Record)
# print(obj_dum)
obj_loa = pickle.loads(obj_dum)
# print(obj_loa)


record = Record('jia')  # 序列化实例
obj = pickle.dumps(record)
# print(obj)

'''
l = [1,2,3,4,]
with open("test", "wb") as f:
    pickle.dump(l, f)
with open("test", "rb") as f:
    # print(pickle.load(f))


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

# print(factorial(5))

def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n-1)


print(power(2,3))
'''

def li(l):
    for i in l:
        if isinstance(i, list):
            li(i)
        else:
            print(i)

# li([1,2,[3,4,5]])

