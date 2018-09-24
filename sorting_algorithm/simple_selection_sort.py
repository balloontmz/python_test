#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
简单选择排序
时间复杂度o(n^2)
对尚未完成排序的所有元素，从头到尾比一遍，记录下最小的那个元素的下标，也就是元素的位置。
再把该元素交换到当前遍历的最前面。其效率之处在于，每一轮中比较了很多此，但只交换了一次。
因此虽然它的时间复杂度也是o(n^2)，但是比冒泡算法还是要好一点
"""

__author__ = 'tomtiddler'

from sorting_algorithm.decorator__ import metric


class SQList(object):
    def __init__(self, lis=None):
        self.lis = lis
        self.count = 0

    def swap(self, i, j):
        """定义一个交换元素的方法，方便后面调用"""
        # 此处的经典三步不应该省略的，能突出显示辅助空间大小
        self.lis[i], self.lis[j] = self.lis[j], self.lis[i]  # 互相交换，思想上需要三步，python语法两步就够了

    @metric
    def select_sort(self):
        """
        简单选择排序，时间复杂度为o(n^2)
        :return:
        """
        lis = self.lis
        length = len(lis)
        for i in range(length-1):
            minimum = i
            for j in range(i + 1, length):
                if lis[minimum] > lis[j]:
                    minimum = j

            if i != minimum:
                self.swap(i, minimum)
                self.count += 1

    def __str__(self):
        ret = ""
        for i in self.lis:
            ret += " %s" % i
        return ret + str(self.count)


if __name__ == "__main__":
    sqlist = SQList([4, 1, 7, 3, 8, 5, 9, 2, 6, 0, 123, 22])
    sqlist.select_sort()
    print(sqlist)
