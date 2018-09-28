#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
merge sqquence
合并两个有序列表

shift + f6 批量修改函数内部的变量名
"""

__author__ = 'tomtiddler'


# 尾递归实现
def _recursion_merge_sort2(ml1, ml2, tmp):
    if len(ml1) == 0 or len(ml2) == 0:
        tmp.extend(ml1)
        tmp.extend(ml2)
        return tmp
    else:
        if ml1[0] < ml2[0]:
            tmp.append(ml1[0])
            del ml1[0]
        else:
            tmp.append(ml2[0])
            del ml2[0]
        return _recursion_merge_sort2(ml1, ml2, tmp)


def recursion_merge_sort2(ml1, ml2):
    return _recursion_merge_sort2(ml1, ml2, [])


# 循环算法
# 上述算法的反向实现
# 以此推测，尾递归的优化实际上就是转换为循环？？？
def loop_merge_sort(ml1, ml2):
    tmp = []

    while len(ml1) > 0 and len(ml2) > 0:
        if ml1[0] < ml2[0]:
            tmp.append(ml1[0])
            del ml1[0]
        else:
            tmp.append(ml2[0])
            del ml2[0]

    # 此时后一个列表必定为空
    tmp.extend(ml1)
    tmp.extend(ml2)
    return tmp


# pop 弹出，利用了pop函数，将本身的两行代码缩减为一行
def merge_sortedlist(ml1, ml2):
    tmp = []
    while ml1 and ml2:
        if ml1[0] >= ml2[0]:
            tmp.append(ml2.pop(0))
        else:
            tmp.append(ml1.pop(0))

    while ml1:
        tmp.append(ml1.pop(0))
    while ml2:
        tmp.append(ml2.pop(0))

    return tmp


if __name__ == "__main__":
    l1 = [1, 2, 3, 7]
    l2 = [3, 4, 5]
    print(recursion_merge_sort2(l1, l2))
    print("*"*20)
    l3 = [1, 2, 3, 7]
    l4 = [3, 4, 5]
    print(loop_merge_sort(l3, l4))
    print("*" * 20)
    l5 = [1, 2, 3, 7]
    l6 = [3, 4, 5]
    print(merge_sortedlist(l5, l6))
    print("*" * 20)
