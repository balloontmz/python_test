#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
希尔排序
时间复杂度跟增量的选取有关O(n^（1.3—2）)
希尔排序是插入排序的改进版本，其核心思想是将原数据集合分隔成若干个子序列，然后再对子序列分别进行直接插入排序，使子序列基本有序，
再对全体记录进行一次直接插入排序。
最关键的是跳跃和分隔策略，间隔多大的问题。通常将相聚某个增量的记录组成一个子序列，这样直接插入排序得到的结果是基本有序的。
本例通过 i = int(i/3)+1 来确定增量的值--此处替换为地板除
int 向下取整  round 四舍五入
https://baike.baidu.com/item/%E5%B8%8C%E5%B0%94%E6%8E%92%E5%BA%8F/3229428?fr=kg_qa
"""

__author__ = 'tomtiddler'

from sorting_algorithm.decorator__ import metric


class SQList(object):
    def __init__(self, lis=None):
        self.lis = lis
        self.count = 0

    @metric
    def shell_sort(self):
        """希尔排序"""
        lis = self.lis
        length = len(lis)
        increment = len(lis)
        while increment > 1:
            increment = increment//3 + 1
            # i 从第二个数字开始，如果第二个小于第一个，就互换
            # 边界条件是一个需要关注的大点
            for i in range(increment, length):
                if lis[i] < lis[i-increment]:
                    temp = lis[i]
                    j = i - increment
                    while j >= 0 and temp < lis[j]:
                        lis[j+increment] = lis[j]
                        self.count += 1
                        j -= increment
                    lis[j+increment] = temp

    def __str__(self):
        ret = ""
        for i in self.lis:
            ret += " %s" % i
        return ret + str(self.count)


if __name__ == "__main__":
    sqlist = SQList([4, 1, 7, 3, 8, 5, 9, 2, 6, 0, 123, 22])
    sqlist.shell_sort()
    print(sqlist)
