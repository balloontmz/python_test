#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
duplicate_removal_list
列表去重方法合集
"""

__author__ = 'tomtiddler'


print("*"*10)
# 用集合去重
l1 = ["b", "c", "d", "b", "c", "a", "a"]
print(list(set(l1)))

print("*"*10)

# 利用字典key的不重复性
# 这些值如何取出？
l1 = ["b", "c", "d", "b", "c", "a", "a"]
l2 = {}.fromkeys(l1).keys()
print(l2)

print("*"*10)
# 列表推导式，语法还要加深
l1 = ["b", "c", "d", "b", "c", "a", "a"]
l2 = []
[l2.append(i) for i in l1 if not (i in l2)]
print(l2)

print("*"*10)
# sorted排序并且用列表推导式
l1 = ["b", "c", "d", "b", "c", "a", "a"]
single = []
[single.append(i) for i in sorted(l1) if i not in single]
print(single)
