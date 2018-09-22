"""
class ListMetaclass(type):
    def __new__(cls, name, bases,attrs):
        attrs['add'] = lambda self , value : self.append(value)
        return super(ListMetaclass,cls).__new__(cls, name , bases , attrs)

class MyList(list , metaclass=ListMetaclass):
    pass
"""


def fn(self, name = 'world'):
    print('Hello,%s' % name)


Hello = type('Hello', (object,), {'fcu':fn})  # {'fcu':fn} is same to: dict(fcu=fn


class UpperAttrMetaclass(type):

    def __new__(cls, name, bases, attrs):
        dicts={}
        for k, v in attrs.items():
            if not k.startswith('__'):
                dicts[k.upper()] = v
            else:
                dicts[k] = v

        return super(UpperAttrMetaclass, cls).__new__(cls, name, bases, dicts)


s = UpperAttrMetaclass('Up', (object,), {'pop':'bar'})

print(hasattr(s, 'pop'))
print(hasattr(s, 'POP'))
print(s.POP)

class FOO(object, metaclass=UpperAttrMetaclass):
    pop='bar'

print(hasattr(FOO, 'pop'))
print(hasattr(FOO, 'POP'))
print(FOO.POP)
# 最后他们的输出结果其实是一模一样的，这就说明了类其实和我们普通的实例对象差不多，只不过普通实例是通过类创建，而类是通过元类创建
# 而__new__就是用来创建实例的，不论是普通的实例，还是类实例，总之就是个实例

# __new__()方法接收到的参数依次是：
#1.当前准备创建的类的对象;2.类的名字;3.类继承的父类集合;4.类的方法的集合。
#实际上在我们实例化对象时，python默认执行了__new__操作，先创建类实例，然后才使用__init__初始化实例

#python新类允许用户重载__new__和__init__方法。__new__创建类实例，__init__初始化一个已被创建的实例。看下面的代码
class newStyleClass(object):
    def __new__(cls):
        print('__new__ is called')
        return super(newStyleClass, cls).__new__(cls)

    def __init__(self):
        print('__init__ is called')
        print('self is: ',self)

newStyleClass()

# 我们发现__new__函数先被调用，接着__init__函数在__new__函数返回一个实例的时候被调用，并且这个实例作为self参数被传入了__init__函数

# 这里需要注意的是，如果__new__函数返回一个已经存在的实例（不论是哪个类的），__init__不会被调用。看下面的代码
obj = 12
# obj can be an object from any class, even object.__new__(object)

class returnExistedObj(object):
    def __new__(cls):
        print('__new__ is called')
        return obj

    def __init__(self):
        print('__init__ is called')

returnExistedObj()

