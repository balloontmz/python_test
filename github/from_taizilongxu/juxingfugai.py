#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
矩形覆盖
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形
无重叠地覆盖一个2*n的大矩形，总共有多少种方法？

采用递归的思想 最后面的覆盖方法有两种，单个覆盖或者两个重叠覆盖
分别对应  f(n) = f(n-1) + f(n-2)
"""

__author__ = 'tomtiddler'


# 本质依然是 fib 数列
def fib(n):
    if n <= 2:
        return n
    else:
        return fib(n-1) + fib(n-2)


if __name__ == "__main__":
    print(fib(5))
