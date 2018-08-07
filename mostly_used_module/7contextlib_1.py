# -*- coding: utf-8 -*-

import contextlib

# 原始的文件打开方式
try:
    f = open('/tomtiddler', 'r')
    f.read()
finally:
    if f:
        f.close()

# with的打开方式
with open('/tomtiddelr', 'r'):
    f.read()

# with的扩展用法 需要包含__enter__;__exit__两个函数
class Query(object):

    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print('Begin')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print('ERROR')
        else:
            print('END')

    def query(self):
        print('Query info about %s...' % self.name)


with Query('Bob') as f:
    f.query()

# 采用contextmanager的with的高级用法
import contextlib
class Query(object):

    def __init__(self, name):
        self.name = name

    def query(self):
        print('Query info about %s...' % self.name)

@contextlib.contextmanager
def creat_query(name):
    print('Begin')
    q = Query(name)
    yield q # 返回给with一个对象
    print('end')

with creat_query('bob') as b: # b接收yield的对象
    b.query()

# 需要在代码执行前后自动执行某段代码时，用一般的decorator也容易实现
import contextlib
@contextlib.contextmanager
def tag(name):
    print('<%s>' % name)
    yield
    print('<\%s>' % name)

with tag('h1'):
    print('hello')
    print('world')

# 调用closing实现不可with对象的with
from urllib.request import urlopen
import contextlib

with contextlib.closing(urlopen('https://www.python.org')) as page:
    for line in page:
        print(line)

# with代码的实际展示
import contextlib
from urllib.request import urlopen
@contextlib.contextmanager
def fcuman(some):
    try:
        yield some
    finally:
        some.close()

with fcuman(urlopen('https://www.python.org')) as page:
    for line in page:
        print(line)
        print(type(page)) # HTTP.Response 对象
