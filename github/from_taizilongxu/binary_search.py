#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
二分查找

"""

__author__ = 'tomtiddler'


# 简单的二分查找，如果找到了，返回下标，否则返回空
def binary_search(lis, target):
    low = 0
    high = len(lis) - 1
    while low <= high:
        mid = (low + high)//2
        guess = lis[mid]
        if guess > target:
            high = mid - 1
        elif guess < target:
            low = mid + 1
        else:
            return mid
    return None


if __name__ == "__main__":
    mylist = [1, 3, 5, 7, 9]
    print(binary_search(mylist, 3))
