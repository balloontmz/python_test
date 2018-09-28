#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
变态跳台阶问题
题目描述： 一个台阶总共有n级，如果一次可以跳1级，也可以跳2级……也可以跳n级。
求总共有多少总跳法，并分析算法的时间复杂度。

题目可以分析为，跳n级。假如第一次跳一级，那么后面有跳n-1级的跳法。以此类推
F(n) = F(n-1)+F(n-2)...+F(2)+F(1)+1  最后一次跳了n级，共一种跳法
用F(n)-F(n-1) 得到 F(n-1)  =>  F(n) = 2 * F(n-1)
"""

__author__ = 'tomtiddler'


def fib(n):
    if n < 2:
        return n
    else:
        return 2 * fib(n-1)


if __name__ == "__main__":
    print(fib(5))
