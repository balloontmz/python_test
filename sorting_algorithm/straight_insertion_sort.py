#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
直接插入排序
时间复杂度o(n^2)
基本操作是将一个记录插入到已经排好序的有序表中，从而得到一个新的、记录增1的有序表
"""

__author__ = 'tomtiddler'

from sorting_algorithm.decorator__ import metric


class SQList(object):
    def __init__(self, lis=None):
        self.lis = lis
        self.count = 0

    def swap(self, i, j):
        """定义一个交换元素的方法，方便后面调用"""
        self.lis[i], self.lis[j] = self.lis[j], self.lis[i]  # 互相交换，思想上需要三步，python语法两步就够了

    @metric
    def insert_sort(self):
        """
        直接插入排序
        :return:
        """
        lis = self.lis
        length = len(lis)
        # 从下标1开始，此处操作的对象是i对应的数字，所以需要选到最后一个，之前的操作的是j对应的数字，所以i取到倒数第二个就行了
        # 此处还有一个知识点，关于变量名，本质是属性或者方法的别名，对其进行的操作就是对属性和方法的操作。
        # 性能比冒泡和简单选择要好吗？通过计数，选择和交换次数与冒泡相同，交换次数应该数简单选择最少。
        for i in range(1, length):
            if lis[i] < lis[i-1]:
                temp = lis[i]
                j = i - 1
                while lis[j] > temp and j >= 0:
                    self.count += 1
                    lis[j+1] = lis[j]
                    j -= 1
                lis[j+1] = temp

    def __str__(self):
        ret = ""
        for i in self.lis:
            ret += " %s" % i
        return ret + str(self.count)


if __name__ == "__main__":
    sqlist = SQList([4, 1, 7, 3, 8, 5, 9, 2, 6, 0, 123, 22])
    sqlist.insert_sort()
    print(sqlist)
