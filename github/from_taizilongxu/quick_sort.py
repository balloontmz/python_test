#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
快速排序
"""

__author__ = 'tomtiddler'


# 代码感觉有点另类。个人觉得不适合于实际的应用中，当作练习吧
def quick_sort(lis):
    if len(lis) < 2:
        return lis
    else:
        midpivot = list[0]
        # python风格的代码
        # 以下两行代码有个问题，就是列表重复遍历了两次，是否是一种资源的浪费
        # 还有一个问题， 对于其他代码的实现，和pivot相等的值，默认是不变换它的原位置的，此处全部归并到了小于项里面--一个小细节
        lessbeforemidpivot = [i for i in lis[1:] if i <= midpivot]
        biggerafterpivot = [i for i in lis[1:] if i > midpivot]
        finallylist = quick_sort(lessbeforemidpivot+[midpivot+quick_sort(biggerafterpivot)])

        return finallylist


print(quick_sort([2, 4, 6, 7, 1, 2, 5]))
