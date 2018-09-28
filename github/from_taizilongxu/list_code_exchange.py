#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
链表的成对互换

思想很有意思
分析：
    首先传入第一个节点对象
    将这一个节点对象的下一个节点对象赋值给临时变量
    把这一个节点对象的下一个节点对象指向处理过的成对链表 -- 递归，处理
    将临时变量的下一个节点对象赋值为第一个节点对象。自此完成单个链表的互换
    返回该临时变量
对于没有下一个节点的节点，返回该对象。递归最终的重点
"""

__author__ = 'tomtiddler'


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    # @param a ListNode
    # @return a ListNode

    def swapPairs(self, head):
        if head and head.next:
            next_ = head.next
            head.next = self.swapPairs(next_.next)
            next_.next = head
            return next_
        return head


if __name__ == "__main__":
    d = ListNode(4)
    c = ListNode(3)
    b = ListNode(2)
    a = ListNode(1)
    a.next = b
    b.next = c
    c.next = d
    print("%s %s %s %s" % (a.val, b.val, c.val, d.val))
    so = Solution()
    e = so.swapPairs(a)
    print("%s %s %s %s" % (e.val, e.next.val, e.next.next.val, e.next.next.next.val))