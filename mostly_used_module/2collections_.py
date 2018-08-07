from collections import *

print('----namedstuple')
point = namedtuple('point', ['x', 'y'])
p = point(1, 2)
print('%s,%s' % (p.x, p.y))
print(p)
print('%s,%s' % (isinstance(p, point), isinstance(p, tuple)))
Circle = namedtuple('Circle',['x', 'y', 'r'])
a= Circle(1,1,3)
print(a)

print('\n----deque')
q = deque(['x', 'y', 'z'])
print(q)
q.append('a')
print(q)
q.appendleft('b')
print(q)
q.popleft()
print(q)
print('%s,%s' % (isinstance(q, list), isinstance(q, deque)))

print('\n----defaultdict')
dd = defaultdict(lambda : 'N\A')
dd['key1'] = 'abc'
print(dd['key1']+' '+dd['key2'])
print(isinstance(dd, defaultdict), isinstance(dd, dict))

print('\n----Ordereddict')
d = dict([('a',1), ('e', 2), ('c', 3), ('d', 4)])
print(d)
print(list(d.keys())) # key本身是无序的
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(od)
print(list(od.keys())) # key是按照输入顺序排序的
# 根据OrderedDict的这个特性能实现一个FIFO（先进先出）的dict
# 此代码尚未仔细核对


class LastUpdatedOrderedDict(OrderedDict):

    def __init__(self, capacity, *args):
        self._capacity = capacity
        super(LastUpdatedOrderedDict, self).__init__(*args)

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity: # 这个语句取决于containKey即传入的key是否存在于列表中
            last = self.popitem(last=False) # 此语句包含last的初始化与赋值
            print('remove:', last)
        if containsKey:
            del self[key]
            print('set:', (key, value))
        else:
            print('add:', (key, value))
        OrderedDict.__setitem__(self, key, value)
b = LastUpdatedOrderedDict(2, [('a',1),])
print(b)
b['b'] = 2
print(b)
b['b'] = 3
print(b)

print('\n----Counter') # 简单的计时器应用
b = Counter()
for x in 'programming':
    b[x]=b[x]+1
print(b)
"""
c = defaultdict(lambda x: x)
for x in 'programming':
    c[x]=c[x]+1
print(c)
# 看下能否实现
"""


