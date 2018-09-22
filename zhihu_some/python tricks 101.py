"""交换变量值"""
a, b = 5, 10
print(a, b)
a, b = b, a
print(a, b)

"""将列表中的所有元素组合成字符串"""
a = ['python', 'is', 'awesome']
print(' '.join(a))

"""列表中最常见的元素 most frequent element in a list"""
a = [1, 2, 3, 1, 2, 3, 2, 2, 4, 5, 1]
print(set(a))  # set是一个无序不重复集合
print(max(set(a), key=a.count))  # 此行代码未理解， count用于统计a中某个元素的出现次数，此处还未传入参数

"""使用Counter类"""
from collections import Counter  # 特殊的列表，在lxf中有.

cnt = Counter(a)
print(cnt)
print(cnt.most_common(3))  # most_common是Counter的方法，用于取前几个truple

"""检查两个字符串是不是由相同字母不同顺序组成"""
from collections import Counter

str1, str2 = '1', '2'
if Counter(str1) == Counter(str2):
    pass

"""反转字符串 reversing string with special case of slice sstep param"""
a = 'agwefgwqrgqwerfgwqerfqwefqwefwer'
print(a[::-1])

"""iterating over string contents in reverse efficiently"""
for char in reversed(a):
    print(char)

"""reversing an integer through type conversion and slicing"""
num = 12312432546
print(int(str(num)[::-1]))

"""反转列表 reversing list with special case of slice step param"""
a = [5, 4, 3, 2, 1]
print(a[::-1])

"""iterating over list contents in reverse efficiently"""
for ele in reversed(a):
    print(ele)

"""转置列表 transpose 2d array [[a,b],[c,d],[e,f]] -> [[a,c,e],[b,d,f]]"""
original = [['a', 'b'], ['c', 'd'], ['e', 'f']]
transposed = zip(*original)  # zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。
print(transposed)
print(list(transposed))

"""链式比较 chained comparison with all kind of operators"""
b = 6
print(4 < b < 7)
print(1 == b < 20)

"""链式函数调用 calling different functions with same arguments based on condition"""


def product(a, b):
    return a * b


def add(a, b):
    return a + b


b = True
print((product if b else add)(5, 7))

"""a fast way to make a shallow copy of a list"""
"""both a and b will be change to [10, 4, 3, 2, 1]"""
b = a
b[0] = 10
print(a, b)
print(a is b)

"""only b will be change to[5, 4, 3, 2, 1]"""
b = a[:]
b[0] = 5
print(a, b)
print(a is b)

"""复制列表的排版方法？ copy list by typecasting method"""
a = [1, 2, 3, 4, 5]
print(list(a))

"""using the lsit.copy() method"""
a = [1, 2, 3, 4, 5]
b = a.copy()
print(a.copy())
print(b is a)

"""深度复制，猜测主要是是否创建内存? copy nested lists using copy.deepcopy"""
from copy import deepcopy

l = [[1, 2], [3, 4]]

l2 = deepcopy(l)
print(l2)
print(l2 is l)

"""returning None or default value. when key is not in dict"""
d = {'a': 1, 'b': 2}
print(d.get('c', 3))

"""Sort a dictionary by its values with the built-in sorted() function and a 'key' argument."""
# 根据值排序
d = {'apple': 18, 'orange': 20, 'banana': 5, 'rotten tomato': 1}
print(sorted(d.items(), key=lambda x: x[1]))

"""Sort using operator.itemgetter as the sort key instead of a lambda"""
from operator import itemgetter

print(sorted(d.items(), key=itemgetter(1)))  # 使用了itemgetter函数

"""Sort dict by value"""
print(sorted(d, key=d.get))

"""else gets called when for loop does not reach break statement"""
# for else 语句 有意思，用于排序算法的时候
a = [1, 2, 3, 4, 5]
for el in a:
    if el == 0:
        break
else:
    print('did not break out of for loop')

"""转换列表为逗号分隔 converts list to comma separated string"""
items = ['foo', 'bar', 'xyz']
print(','.join(items))

"""list of numbers to comma separated"""
numbers = [2, 3, 5, 10]
x = map(str, numbers)  # map函数返回的是一个迭代器？ 测试过 是  惰性的
print(list(x))
print(','.join(map(str, numbers)))

"""list of mix data"""
data = [2, 'hello', 3, 3.4]
print(','.join(map(str, data)))

"""合并字典 merge dict's"""
d1 = {'a': 1}
d2 = {'b': 2}

print({**d1, **d2})

print(dict(d1.items() | d2.items()))

d1.update(d2)
print(d1)

"""列表中最小最大值的索引 Find Index of Min/Max Element."""
lst = [40, 10, 20, 30]


def minIndex(lst):
    return min(range(len(lst)), key=lst.__getitem__)


def maxIndex(lst):
    return max(range(len(lst)), key=lst.__getitem__)


print(minIndex(lst))
print(maxIndex(lst))

"""移除列表中重复的元素 remove duplicate items from list. notes: does not preserve(保存) the original list order"""
items = [2, 2, 3, 3, 1]
newitems2 = list(set(items))
print(newitems2)

"""remove dups and keep order"""
from collections import OrderedDict

items = ['foo', 'bar', 'bar', 'foo']
print(OrderedDict.fromkeys(items).keys())
