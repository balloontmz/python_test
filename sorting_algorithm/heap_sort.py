#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
堆排序
堆是完全二叉树
其根节点一定是最大或者最小值
堆排序（Heap Sort）就是利用大顶堆或小顶堆的性质进行排序的方法。
堆排序的总体时间复杂度为O(nlogn)。（下面采用大顶堆的方式）

其核心思想是：将待排序的序列构造成一个大顶堆。此时，整个序列的最
大值就是堆的根节点。将它与堆数组的末尾元素交换，然后将剩余的n-1个
序列重新构造成一个大顶堆。反复执行前面的操作，最后获得一个有序序列。

堆排序对原始记录的排序状态不敏感，因此它无论最好、最坏和平均时间复杂度都
是O(nlogn)。在性能上要好于冒泡、简单选择和直接插入算法。

空间复杂度上，只需要一个用于交换的暂存单元。但是由于记录的比较和交换是跳
跃式的，因此，堆排序也是一种不稳定的排序方法。

此外，由于初始构建堆的比较次数较多，堆排序不适合序列个数较少的排序工作。
"""

__author__ = 'tomtiddler'

from sorting_algorithm.decorator__ import metric


class SQList(object):
    def __init__(self, lis=None):
        self.lis = lis
        self.count = 0

    def swap(self, i, j):
        """定义一个元素交换的方法，方便后面调用"""
        temp = self.lis[i]
        self.lis[i] = self.lis[j]
        self.lis[j] = temp

    @metric
    def heap_sort(self):
        """堆排序"""
        length = len(self.lis)
        i = int(length/2)  # 此处可采用地板除
        # 将原始序列构造成一个大顶堆
        # 遍历从中间开始（即拥有子节点的最下面一个父节点），到0结束，其实这些是堆的分支节点
        while i >= 0:
            self._heap_ajust(i, length-1)
            i -= 1
        # 逆序遍历整个序列，不断取出根节点的值，完成实际的排序
        j = length - 1
        while j > 0:
            # 将当前根节点，也就是列表的最开头，下标为0的值，交换到j处。
            self.swap(0, j)
            # 将发生变换的序列重新构造成大顶堆
            # 之后的数据已经有序了
            self._heap_ajust(0, j-1)
            j -= 1

    def _heap_ajust(self, s, m):
        """核心的大顶堆构造方法，维持序列的堆结构"""
        # 对于构造大顶堆，从下往上构造，依次抛出最大值直至顶点
        # 对于重构大顶堆，从上往下构造，将被交换的父节点下发到合适的位置
        lis = self.lis
        temp = lis[s]
        i = 2 * s
        while i <= m:
            if i < m and lis[i] < lis[i+1]:
                i += 1
            if temp >= lis[i]:
                break
            self.count += 1
            lis[s] = lis[i]
            s = i
            i *= 2
        lis[s] = temp

    def __str__(self):
        ret = ""
        for i in self.lis:
            ret += " %s " % i
        return ret + str(self.count)


if __name__ == "__main__":
    sqlist = SQList([4, 1, 7, 3, 8, 5, 9, 2, 6, 0, 123, 22])
    sqlist.heap_sort()
    print(sqlist)
