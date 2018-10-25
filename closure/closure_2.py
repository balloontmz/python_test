# -*- coding: utf-8 -*-
__author__ = 'tomtiddler'


# 闭包的经典误区

def f1():
    a = 10

    def f2():
        a = 20  # 闭包内部不能定义局部变量 可以采用 a = a + 10 的方式引用外部变量
        return a
    return f2

f = f1()
print(f)
print(f.__closure__)  # 返回None，一旦函数的内部定义赋值了局部变量，将不再形成闭包，必须引用外部变量！！！
