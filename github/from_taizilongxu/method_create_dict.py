#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
method for create dict
创建字典的方法
"""

__author__ = 'tomtiddler'


# 1.直接创建
dict1 = {"name": "earth", "port": "80"}

# 2.工厂方法
items = [("name", "earth"), ("port", "80")]
dict2 = dict(items)
dict3 = dict([("name", "earth"), ("port", "80")])

# fromkeys()方法
dict4 = {}.fromkeys(("x", "y"), -1)  # fromkeys 后面的参数为共用的value，不管是什么类型的参数
print(dict4)
dict5 = {}.fromkeys(("x", "y"))
print(dict5)

