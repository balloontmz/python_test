#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
交叉链表求交点

主要思路还是先截断到同一长度再并行比较
原理为链表一旦相交，后续的所有节点都相同
"""

__author__ = 'tomtiddler'

import copy

# 模拟寻找交叉节点
# 使用a,b两个list来模拟链表，可以看出交叉点是 7这个节点
a = [1, 2, 3, 7, 9, 1, 5]
b = [4, 5, 7, 9, 1, 5]

for i in range(1, min(len(a), len(b))):
    if i == 1 and (a[-1] != b[-1]):
        print("No")
        break
    else:
        if a[-i] != b[-i]:
            print("交叉节点：{code}".format(code=a[-i+1]))
            break
        else:
            pass


class ListNode(object):
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


def node(l1, l2):
    length1, length2 = 0, 0
    # 此处需要引用传入的变量，因为不能对传入变量直接自赋值遍历多次，只能自定义变量进行一次自赋值遍历
    ml1 = l1
    ml2 = l2
    while ml1.next:
        ml1 = ml1.next
        length1 += 1
    while ml2.next:
        ml2 = ml2.next
        length2 += 1

    if length1 > length2:
        for _ in range(length1-length2):
            l1 = l1.next
    else:
        for _ in range(length2-length1):
            l2 = l2.next

    while l1 and l2:
        if l1.next.val == l2.next.val:
            return l1.next
        else:
            l1 = l1.next
            l2 = l2.next


if __name__ == "__main__":
    a = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    b = ListNode(3, ListNode(2, ListNode(3, ListNode(4))))
    print(node(a, b).val)
