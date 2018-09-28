#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
杨式矩阵查找

在一个m行n列二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从
上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判
断数组中是否含有该整数。

使用四分法查找

杨式矩阵查找的几种算法及分析：线性搜索、普通二分和对角线二分、矩阵的四分法
http://blog.sina.com.cn/s/blog_8999d1c60102ycw2.html
原文：https://blog.csdn.net/sgbfblog/article/details/7745450#0-tsina-1-22881-397232819ff9a47a7b7e80a40613cfe1
"""

__author__ = 'tomtiddler'

# 此代码用于设置递归次数
# import sys
#
# sys.setrecursionlimit(1000000)  #例如这里设置为一百万


# 此时实现的是四分法，复杂度为： 计算公式T(n) = 3T(n/2) + c,结果O(n^1.58)
class Quartation(object):
    def __init__(self, lis, key):
        self.lis = lis
        self.key = key
        self.count = 0

    def find_key(self):
        edm = len(self.lis) - 1
        edn = len(self.lis[0]) - 1
        return self.find(0, 0, edm, edn, self.key)

    def find(self, bgm, bgn, edm, edn, target):
        if target < self.lis[bgm][bgn] or target > self.lis[edm][edn]:
            return False
        midm = (edm + bgm)//2
        midn = (edn + bgn)//2
        if self.lis[midm][midn] == target:
            return True
        # else:
        #     print("count %s %s" % (bgm, edm))
        # 已经分割到最小单位的处理方法,此处功能是否与第一行重复了？第一行只是增加了一个递归深度而已？
        # 测试完成，这一行功能上确实没必要，但是可能某些时候可以减少递归深度，看情况吧？
        elif midm == edm and midn == edn:
            return False

        if self.lis[midm][midn] > target:
            return \
                self.find(bgm, bgn, midm, midn, target) or\
                self.find(bgm, midn+1, midn, edn, target) or\
                self.find(midm+1, bgn, edm, midn, target)
        else:
            # 此处 第一行出现bug，导致原因为midm、midn没有+1,致使其永远无法和edm、edn相等，进而出现死循环，切记细心
            return \
                self.find(midm+1, midn+1, edm, edn, target) or \
                self.find(bgm, midn + 1, midn, edn, target) or \
                self.find(midm + 1, bgn, edm, midn, target)


if __name__ == "__main__":
    quartation = Quartation(lis=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], key=8)
    print(quartation.find_key())


