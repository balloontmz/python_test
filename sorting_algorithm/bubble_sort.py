#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
冒泡排序：时间复杂度 o(n^2)
核心思想是：两两比较相邻的关键字，如果反序则交换，直到没有反序记录为止。
其实现细节可以不同：
1.最简单排序实现：bubble_sort_simple
2.冒泡排序：bubble_sort
3.改进的冒泡排序：bubble_sort_advance
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
    def bubble_sort_simple(self):
        """
        最简单的交换排序，时间复杂度o(n^2)
        :return:
        """
        lis = self.lis
        length = len(self.lis)
        for i in range(length - 1):
            for j in range(i+1, length):
                if lis[i] > lis[j]:
                    self.swap(i, j)
                    self.count += 1

    @metric
    def bubble_sort(self):
        """
        冒泡排序，时间复杂度o(n^2)
        :return:
        """
        lis = self.lis
        length = len(lis)

        # 此处range的长度应该减1？还未测试，因为最后一位的值不再需要运算。或者在实际应用中最后一位的运算也有价值？
        for i in range(length - 1):
            j = length - 2
            while j >= i:
                if lis[j] > lis[j+1]:
                    self.swap(j, j+1)
                    self.count += 1
                j -= 1

    @metric
    def bubble_sort_advance(self):
        """
        冒泡排序改进算法，时间复杂度o(n^2)
        设置flag，当一轮比较中未发生交换动作，则说明后面的元素其实已经有序排列了。
        对于比较规整的元素集合，可提高一定的排序效率
        :return:
        """
        lis = self.lis
        length = len(lis)
        flag = True
        i = 0
        # 此处 i 是否应该设置为 小于 length-1 最后一位不需要运算了的吧
        while i < length - 1 and flag:
            flag = False
            j = length - 2
            while j >= i:
                if lis[j] > lis[j+1]:
                    self.swap(j, j+1)
                    self.count += 1
                    flag = True
                j -= 1
            i += 1

    def __str__(self):
        ret = ""
        for i in self.lis:
            ret += " %s" % i
        return ret + str(self.count)


if __name__ == "__main__":
    sqlist = SQList([4, 1, 7, 3, 8, 5, 9, 2, 6, 0, 123, 22])
    sqlist.bubble_sort_advance()
    print(sqlist)

    sqlist = SQList([4, 1, 7, 3, 8, 5, 9, 2, 6, 0, 123, 22])
    sqlist.bubble_sort_simple()
    print(sqlist)

    sqlist = SQList([4, 1, 7, 3, 8, 5, 9, 2, 6, 0, 123, 22])
    sqlist.bubble_sort()
    print(sqlist)
