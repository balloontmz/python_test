#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
dynamic programming coinchange
硬币找零的动态规划

本次实现的思路如下：
定义一个数组，从1开始用来存放计算出来的找零值
一次循环到顶部，即求解出最终值
此实现的好处是：防止采用每次递归都需要计算子问题的最小值--采用数组直接记忆结果，缩减运算量。

由此引发的问题：如果是需要计算找钱方法数呢？此时采用哪种算法更合理？
"""

__author__ = 'tomtiddler'


def coinChange(values, valuesCounts, money, coinsUserd):
    """

    :param values: 硬币种类数组
    :param valuesCounts: 硬币种类数
    :param money: 找出来的总钱数
    :param coinsUserd: 对于目前总前数 所使用的硬币数目
    :return:
    """
    for cents in range(1, money+1):
        minCoins = cents  # 从第一个开始到money的所有情况初始，就是默认全部使用1元硬币

        # 此段代码的逻辑为：找零的最后一次结果必定属于硬币数组，分别计算各种问题的步数，取最小值
        # 如果是要算方案数，将需要采用一个临时变量，然后分别计算各种问题方案数，叠加--猜测，暂没实现，此方法与递归相比呢？
        for kind in range(0, valuesCounts):
            if values[kind] <= cents:
                temp = coinsUserd[cents-values[kind]] + 1
                if temp < minCoins:
                    minCoins = temp

        coinsUserd[cents] = minCoins
        print("面值为：{0} 的最小硬币数目为： {1}".format(cents, coinsUserd[cents]))
    return coinsUserd


if __name__ == "__main__":
    values = [25, 21, 10, 5, 1]
    money = 63
    coinUserd = [0]*(money+1)
    lens = len(values)
    print(len(coinChange(values, lens, money, coinUserd)))
