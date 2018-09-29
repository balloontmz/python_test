#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
a test module
"""

__author__ = 'tomtiddler'


def count():
    """
    在需要引入循环变量的情况下，需要再进行一次封装，这样才能记录创建返回函数时的环境变量值，
    其实这个封装去除也是没关系的，那样fs同样会记录整个for循环的返回函数，并且记录当前环境变量
    否则返回的函数调用时将会循环调用环境变量的最终值，而不是返回函数时的当前值。
    同时，count函数返回了一个列表，列表的每个可调用函数都存在__closure__属性值，
    #####所以 可以进一步推测，对闭包的调用型封装并返回也是闭包。#####
    # 此函数等价于如下：
    def f1(j):
        def g():
            return j * j
        return g
    """
    def f1(j):
        return lambda: j*j  # 此处lambda不接收任何参数，而是调用外部f1的参数。其实本质是一个小闭包

    fs = []

    for i in range(1, 4):
        fs.append(f1(i))  # ci
    return fs


if __name__ == "__main__":
    a, b, c = count()
    print("%s ===> %s" % (a, a()))
    print("%s ===> %s" % (b, b()))
    print("%s ===> %s" % (c, c()))
