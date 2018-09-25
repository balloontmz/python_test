#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
归并排序
分冶法 + 递归 或者尾递归
辅助空间为o(n)

"""

__author__ = 'tomtiddler'


class SQList(object):
    def __init__(self, lis=None):
        self.r = lis

    def merge_sort(self):
        # 此代码复制的，需要自己再编写一遍
        # 如果自己再定义一个数组接收辅助空间的值，那么是不是代表辅助空间增加了一倍？ 逻辑上说是的，机理上不出意外也是的
        # a = [None for i in range(0, len(self.r))]
        self.msort(self.r, self.r, 0, len(self.r)-1)
        # print("-"*30)
        # print(a)

    def msort(self, list_sr, list_tr, s, t):
        temp = [None for i in range(0, len(list_sr))]
        if s == t:
            list_tr[s] = list_sr[s]
        else:
            m = int((s+t)/2)
            self.msort(list_sr, temp, s,  m)
            self.msort(list_sr, temp, m+1, t)
            print(temp)  # 局部变量，仅作用于函数本身及下级函数，函数退出不保存
            self.merge(temp, list_tr, s, m, t)
            print(list_tr)  # 向上抛出的值。外部传入的可变列表

    def merge(self, list_sr, list_tr, i, m,  n):
        j = m+1
        k = i
        while i <= m and j <= n:
            if list_sr[i] < list_sr[j]:
                list_tr[k] = list_sr[i]
                i += 1
            else:
                list_tr[k] = list_sr[j]
                j += 1

            k += 1
        if i <= m:
            for l in range(0, m-i+1):
                list_tr[k+l] = list_sr[i+l]
        if j <= n:
            for l in range(0, n-j+1):
                list_tr[k+l] = list_sr[j+l]

    def __str__(self):
        ret = ""
        for i in self.r:
            ret += " %s" % i
        return ret


if __name__ == '__main__':
    sqlist = SQList([4, 1, 7, 3, 8, 5, 9, 2, 6, 0, 12, 77, 34, 23])
    sqlist.merge_sort()
    print(sqlist)
