# -*- coding: utf-8 -*-
__author__ = 'tomtiddler'


# 最简单的闭包
# 返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
def curve_pre():
    a = 25

    def curve(x):
        y = a * x ^ 2 + x
        return y
    return curve


re = curve_pre()
print(re)  # <function curve_pre.<locals>.curve at 0x7f73b9e27158>
print(re.__closure__)  # 闭包的参数对象
print(re.__closure__[0].cell_contents)  # 返回闭包的参数
print(re(2))
