#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
快速排序
由图灵奖获得者Tony Hoare 发明，被列为20世纪十大算法之一。冒泡排序的升级版，交换排序的一种
复杂度为o(nlogn)
快速排序的核心思想：
通过一趟排序将待排记录分割成独立的两部分，其中一部分记录的关键字均比另一部分记录的关键字小，然后分别对这两部分继续进行排序，
以达到整个记录集合的排序的目的
需要辅助空间，其空间复杂度为o(logn),递归需要logn？
"""

__author__ = 'tomtiddler'

from sorting_algorithm.decorator__ import metric


class SQList(object):
    def __init__(self, lis=None):
        self.lis = lis
        self.count = 0

    def swap(self, i, j):
        """定义一个元素交换的方法，方便后面调用"""
        temp = self.lis[i]
        self.lis[i] = self.lis[j]
        self.lis[j] = temp

    @metric
    def quick_sort(self):
        """调用入口"""
        self.qsort(0, len(self.lis)-1)  # 函数的 low 和 high 分别代表最小和最大的下标，均是包含

    def qsort(self, low, high):
        """递归调用"""
        if low < high:
            pivot = self.partition(low, high)  # 此处返回的值 之前的 均小于此值 之后的 均大于此值
            self.qsort(low, pivot-1)
            self.qsort(pivot+1, high)

    def partition(self, low, high):
        """
        快速排序的核心代码
        该函数调用过程中 pivot_key 的值始终不变，只是用作读取
        :param low: 左边界下标
        :param high: 右边界下标
        :return 分完左右区后pivot_key所在位置的下标 -- 需要一定的分析，此段为核心代码
        """
        lis = self.lis
        pivot_key = lis[low]  # 一个分界值，辅助空间，不会改变原有列表的值
        # 通过此分界值，不断变换其在之前的lis中的位置，最终将比它小的全部换到左边，比它大的全部换到右边
        while low < high:  # 最后结果一定是 low = high
            while low < high and lis[high] >= pivot_key:
                high -= 1
            self.swap(low, high)  # 一旦while为否才执行到此语句，即 lis[high] < pivot_key
            self.count +=1
            while low < high and lis[low] <= pivot_key:
                low += 1
            self.swap(low, high)  # 一旦while为否才执行到此语句，即 lis[low] > pivot_key
            self.count += 1
        return low

    def __str__(self):
        ret = ""
        for i in self.lis:
            ret += " %s " % i
        return ret + str(self.count)


if __name__ == "__main__":
    sqlist = SQList([4, 1, 7, 3, 8, 5, 9, 2, 6, 0, 12, 77, 34, 23])
    sqlist.quick_sort()
    print(sqlist)
