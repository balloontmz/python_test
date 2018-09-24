#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
a test module
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