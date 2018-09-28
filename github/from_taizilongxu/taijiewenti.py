#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
台阶问题的三种解法
题目详情：
一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
"""

__author__ = 'tomtiddler'


# pep8 style错误，能运行
# fib = lambda n: n if n <= 2 else fib(n - 1) + fib(n - 2)
# 思路历程为最后一次可能跳的一步或者两步，恰好对应递归的 n-1 n-2 阶的步数，此函数的返回是个标准的fib数列
def fib_1(n):
    if n <= 2:
        return n
    else:
        return fib_1(n-1) + fib_1(n-2)


# 这个记忆方法，虽然是采用了装饰器和闭包，但总感觉是画蛇添足？
def memo(func):
    cache = {}

    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return wrap


@memo
def fib_2(i):
    if i < 2:
        return 1
    return fib_2(i-1) + fib_2(i-2)


# 第三种方法，为fib的生成方法，很难看到解题的思路？
def fib_3(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b
    return b


if __name__ == "__main__":
    print(fib_1(5))
    print(fib_2(5))
    print(fib_3(5))

