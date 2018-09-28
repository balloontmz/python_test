#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
杨式矩阵查找

在一个m行n列二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从
上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判
断数组中是否含有该整数。

使用二分法查找

杨式矩阵查找的几种算法及分析：线性搜索、普通二分和对角线二分、矩阵的四分法
http://blog.sina.com.cn/s/blog_8999d1c60102ycw2.html
原文：https://blog.csdn.net/sgbfblog/article/details/7745450#0-tsina-1-22881-397232819ff9a47a7b7e80a40613cfe1
"""

__author__ = 'tomtiddler'


# 此时实现的是二分法，复杂度为： 计算公式T(n) = 2T(n/4) + cn. 同时，可采用二分查找进行优化
# 此方法将采用对角线二分。除了对角线，还可采用行二分和列二分，推测主要决定于行列的个数?
class Dechotomy(object):
    def __init__(self, lis, key):
        self.lis = lis
        self.key = key
        self.count = 0

    def find_key(self):
        edm = len(self.lis) - 1
        edn = len(self.lis[0]) - 1
        return self.find(0, 0, edm, edn, self.key)

    def find(self, bgm, bgn, edm, edn, target):
        if bgm > edn or bgn > edn:  # 参数检查，防止越界 四分法不需要这一行，因为其选取规则决定了其不可能越界，具体问题，具体分析
            return False
        if self.lis[bgm][bgn] > target or self.lis[edm][edn] < target:
            return False
        i, j = bgm, bgn
        while self.lis[i][j] <= target and i <= edm and j <= edn:
            if self.lis[i][j] == target:
                return True
            i, j = i + 1, j + 1

        return self.find(bgm, j, i-1, edn, target) or self.find(i, bgn, edm, j-1, target)



if __name__ == "__main__":
    dechotomy = Dechotomy(lis=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], key=8)
    print(dechotomy.find_key())


