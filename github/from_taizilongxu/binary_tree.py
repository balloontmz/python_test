#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
binary tree

广度遍历和深度遍历二叉树

"""

__author__ = 'tomtiddler'


class Node(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    # 广度遍历
    def lookup(self):
        row = [self]  # 将row初始化为self，使row能被遍历并且从根节点开始。
        while row:
            # 此行打印row的节点数据。由于row为列表且row不定长，个人感觉采用map函数更合适
            print(list(map(lambda item: item.data, row)))
            row = [kid for item in row for kid in (item.left, item.right) if kid]

    # 前中后序遍历：实际上就是深度遍历改变顺序
    # 深度遍历--此为前序遍历--访问当前节点、遍历左子树，再遍历右子树--pre_travelsal
    def deep(self):
        print(self.data, end="  ")
        if self.left:
            self.left.deep()
        if self.right:
            self.right.deep()

    # 中序遍历
    def mid_travelsal(self):
        if self.left:
            self.left.deep()
        # 访问当前节点
        print(self.data, end="  ")
        if self.right:
            self.right.deep()

    # 后序遍历
    def post_travelsal(self):
        if self.left:
            self.left.deep()
        if self.right:
            self.right.deep()
            # 访问当前节点
            print(self.data, end="  ")

    # 求最大树深
    def maxdepth(self):
        if not self.left and not self.right:  # 此处出过bug，究其原因需要细心思考逻辑运算，不能瞎写
            return 1
        if self.left and self.right:
            return max(self.left.maxdepth(), self.right.maxdepth()) + 1
        elif self.left:
            return self.left.maxdepth() + 1
        elif self.right:
            return self.right.maxdepth() + 1


def isSameTree(tree_one, tree_two):
    """
    求两颗树是否相同
    :param tree_one:
    :param tree_two:
    :return:
    """
    if not tree_one and not tree_two:
        return True
    elif tree_one and tree_two:
        return tree_one.val == tree_two.val and isSameTree(tree_one.left, tree_two.left) and isSameTree(tree_one.right, tree_two.right)
    else:
        return False


def post_travelsal(pr, centers):
    """
    已知前序中序求后续的函数，此代码目前全部是拷贝，没有review。
    下列网址为该算法的思维导读，目前已基本了解：
    http://blog.csdn.net/hinyunsin/article/details/6315502
    :param pr: 前序列表，为list
    :param centers: 中序列表，为list
    :return:
    """

    def rebuild(pre, center):
        if not pre:
            return
        cur = Node(pre[0])
        index = center.index(pre[0])
        cur.left = rebuild(pre[1:index + 1], center[:index])
        cur.right = rebuild(pre[index + 1:], center[index + 1:])
        return cur

    tree_rb = rebuild(pr, centers)

    def deep(root):
        if not root:
            return
        deep(root.left)
        deep(root.right)
        print(root.data)  # 应该返回一个列表的，此处为了简单，返回的是打印。

    deep(tree_rb)


if __name__ == "__main__":
    tree = Node(1, Node(3, Node(7, Node(0)), Node(6)), Node(2, Node(5), Node(4)))
    print("*"*20+"lookup"+"*"*20)
    tree.lookup()
    print("\n" + "*" * 20 + "deep"+"*"*20)
    tree.deep()
    print("\n" + "*" * 20 + "mid_travelsal" + "*" * 20)
    tree.mid_travelsal()
    print("\n" + "*" * 20 + "post_travelsal" + "*" * 20)
    tree.post_travelsal()
    print("\n" + "*" * 20 + "maxdepth" + "*" * 20)
    print(tree.maxdepth())
