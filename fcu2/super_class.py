
def fn(self,name='world'):
    print('Hello,{0}'.format(name))
Hello = type('Hello',(object,),dict(hello=fn))


class UpperAttrMetaclass(type):

    def __new__(cls, clsname, bases, dct):
        uppercase_attr = {}
        for name, val in dct.items():
            if not name.startswith('__'):
                uppercase_attr[name.upper()] = val
            else:
                uppercase_attr[name] = val

        return super(UpperAttrMetaclass, cls).__new__(cls, clsname, bases, uppercase_attr)

# 我们知道在python中一切皆对象
# 那么下面我们的s其实就是一个类对象，它的__name__其实和Foo的__name__是一样的
# 看下面的方法是不是和type创建类有点像？
s = UpperAttrMetaclass('Foo',(object,),{'bar':'bip'})
print(hasattr(s,'bar'))
print(hasattr(s,'BAR'))
print(s.BAR)

class Foo(object,metaclass=UpperAttrMetaclass):
    bar='bip'
print(hasattr(Foo,'bar'))
print(hasattr(Foo,'BAR'))
print(Foo.BAR)