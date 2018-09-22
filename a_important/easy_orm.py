#!/user/bin/env python3
# -*- coding: utf-8 -*-

"""a easy orm"""

__author__ = 'tomtiddler'


class Field(object):

    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    # 使用 print（Field（‘xx’），打印以下字段
    def __str__(self):
        # self.__class__.__name__为类的名字
        # self.__class__指向当前类，所以返回 StringField 和IntergerField
        # 即调用 StringField(id) 时，返回<StringField:id>
        return '<%s:%s>' % (self.__class__.__name__, self.name)
    __repr__ = __str__  # Field('xx')可打印以上字段


class StringField(Field):

    def __init__(self, name):
        # super(StringField, self) 首先找到 StringField的父类（Field)，然后把子类的对象转换为父类的对象
        # varcher(100) 为最大允许100字节
        super(StringField, self).__init__(name, 'varchar(100)')


class IntegerField(Field):

    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')


class ModelMetaclass(type):

    # 在 __init__之前，在类准备将自身实例化时调用，mcs(cls)为目前正在实例化的类
    # __new__参数为：准备创建的类的对象，类的名字；类继承的父类集合;类的方法集合
    # 如果new()没有返回mcs（即当前类）的实例，那么当前类的init（）方法是不会被调用的
    # attrs 会将 bar == True，翻译为{‘bar’：True}
    def __new__(mcs, name, bases, attrs):  # 在创建实例时最先执行
        if name == 'Model':
            # 得到当前类的实例，使用父类xx.__new__(mcs)
            # 即运行Model 类 时，调用
            return type.__new__(mcs, name, bases, attrs)
        print('Found model: %s' % name)  #name不为Model调用
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('Found mapping: %s ==> %s' % (k, v))
                # 使用mappings存储attrs
            mappings[k] = v
        # mapping.keys ，返回dict的key
        for k in mappings.keys():
            attrs.pop(k)
            # 调用 u.save()时，使value指向输入：attrs类属性已被删除
        attrs['__mapping__'] = mappings
        '''
        attrs 为即将要创建的class属性，以上代码相当于
        class Model(dict):
            def __mappings__(self):
                return mappings
        '''
        attrs['__table__'] = name  #设定表名
        return type.__new__(mcs, name, bases, attrs)  # 这一句忘记加了


class Model(dict, metaclass=ModelMetaclass):

    def __init__(self, **kw):  #传入的参数为dict
        #print('init is called') 执行于__new__()之后
        super(Model, self).__init__(**kw)

    # 首先在自己和父类中查找属性，找不到才会在getattrs中查找
    def __getattr__(self, key):
        try:
            print('input is being called')
            return self[key]
        except KeyError:
            raise ArithmeticError(r"'Model' object has no attribute '%s'" % key)

    #def __setattr__(self, key, value):
        #self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mapping__.items():
            if isinstance(v, Field):
                fields.append(v.name)
                params.append('?')
                args.append(getattr(self, k, None))
            # 从self中查找k属性，由于在metaclass中k被删除，所以不存在，只能调用geattr从外部传入的参数
        # ','.join(list) 就是把 list中所有字符串按照逗号连接
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))  #str 返回一个对象的 string格式


# metaclass编写的orm
class User(Model):
    # 定义类的属性到列的映射
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')


# 创建一个实例
u = User(id=12345, name='tom', email='test@orm.org', password='my-pwd')

# 保存到数据库
u.save()
# 由orm完成
# 定义Field类，它负责保存数据库的字段名和字段类型
