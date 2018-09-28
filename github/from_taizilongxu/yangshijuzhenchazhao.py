#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
杨式矩阵查找

在一个m行n列二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从
上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判
断数组中是否含有该整数。

使用Step-wise线性搜索。复杂度为o(n)
从右上角 l[0][n] 开始查找，查找路径画出一条向下和向左的折线，终点为该整数或者左下角
这个东西，有点意思的。自己多看几遍，目前大概是懂了的，画个图能更清晰

杨式矩阵查找的几种算法及分析：线性搜索、普通二分和对角线二分、矩阵的四分法
http://blog.sina.com.cn/s/blog_8999d1c60102ycw2.html
原文：https://blog.csdn.net/sgbfblog/article/details/7745450#0-tsina-1-22881-397232819ff9a47a7b7e80a40613cfe1
"""

__author__ = 'tomtiddler'


# 此时实现的是线性搜索，还有二分法暂时没有实现？
def get_value(l, r, c):
    return l[r][c]


def find(l, x):
    m = len(l) - 1
    n = len(l[0]) - 1
    r = 0
    c = n

    while c >= 0 and r <= m:
        value = get_value(l, r, c)
        if value == x:
            return True
        elif value > x:
            c = c - 1
        elif value < x:
            r = r + 1

    return False


if __name__ == "__main__":
    lis = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    key = 8
    print(find(lis, key))
