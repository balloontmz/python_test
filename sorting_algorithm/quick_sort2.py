#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
快速排序
"""

__author__ = 'tomtiddler'


def quick_sort(nums):
    # 封装一层的目的是方便用户调用
    count = 0

    def qsort(lst, begin, end):
        nonlocal count
        if begin >= end:
            return
        i = begin
        key = lst[begin]
        for j in range(begin+1, end+1):
            if lst[j] < key:
                # i 的取值最后总能保证 i自己所处的位置，自己总比begin小，除非整个序列begin最小。i右边的所有数据都比begin大或者相等
                # 此for循环内部逻辑为：
                # 一旦有小于begin的数据，就将其交换到下标自增1的序列
                i += 1
                lst[i], lst[j] = lst[j], lst[i]
                count += 1
        lst[begin], lst[i] = lst[i], lst[begin]
        count += 1
        qsort(lst, begin, i-1)
        qsort(lst, i+1, end)

    qsort(nums, 0, len(nums)-1)
    return count


if __name__ == "__main__":
    sqlist = [4, 1, 7, 3, 8, 5, 9, 2, 6, 0, 12, 77, 34, 23]
    print(quick_sort(sqlist))
    print(sqlist)


