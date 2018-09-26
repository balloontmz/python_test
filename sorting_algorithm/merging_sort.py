#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
归并排序
分冶法 + 递归 或者尾递归
辅助空间为o(n)
核心思想是采用递归将需要排序的数据分割成极其容易排序的子序列，然后对有序的子序列进行排序
是稳定排序？
归并排序占用内存，但是效率高。并且稳定
"""

__author__ = 'tomtiddler'

from sorting_algorithm.decorator__ import metric


class SQList(object):
    def __init__(self, lis=None):
        self.lis = lis
        self.count = 0

    @metric
    def merge_sort(self):
        # 如果自己再定义一个数组接收辅助空间的值，那么是不是代表辅助空间增加了一倍？ 逻辑上说是的，机理上不出意外也是的
        self.msort(self.lis, self.lis, 0, len(self.lis)-1)

    def msort(self, list_sr, list_tr, s, t):
        temp = [None] * len(list_sr)  # temp = [None for i in range(0, len(list_sr))]
        if s == t:
            list_tr[s] = list_sr[s]
            self.count += 1  # 赋值为最底层的操作，复杂度为n ，此处为14次，而其他操作为 54 次
        else:
            m = (s + t)//2  # 等价于 int((s+t)/2)
            self.msort(list_sr, temp, s, m)
            self.msort(list_sr, temp, m+1, t)
            print(temp)  # 局部变量，仅作用于函数本身及下级函数，函数退出不保存
            self.merge(temp, list_tr, s, m, t)
            print(list_tr)  # 向上抛出的值。外部传入的可变列表

    def merge(self, list_sr, list_tr, i, m, e):
        j = m + 1
        k = i
        while i <= m and j <= e:
            if list_sr[i] < list_sr[j]:
                list_tr[k] = list_sr[i]
                i += 1
            else:
                list_tr[k] = list_sr[j]
                j += 1
            k += 1
            self.count += 1

        if i <= m:
            for l in range(0, m - i + 1):
                list_tr[k + l] = list_sr[i + l]
                self.count += 1
        if j <= e:
            for l in range(0, e - j + 1):  # 此处的end 输成了middle 导致程序出错，需要debug 和 细致
                list_tr[k + l] = list_sr[j + l]
                self.count += 1

    def __str__(self):
        ret = ""
        for i in self.lis:
            ret += " %s " % i
        return ret + str(self.count)


if __name__ == "__main__":
    sqlist = SQList([4, 1, 7, 3, 8, 5, 9, 2, 6, 0, 12, 77, 34, 23])
    sqlist.merge_sort()
    print(sqlist)

