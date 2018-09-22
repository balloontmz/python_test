#定义 Field 类，负责保存数据库表的字段名和字段类型
class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    # 使用 print(Field('xx'))，打印以下字段
    def __str__(self):
        # self.__class__.__name__ 为类的名字
        # self.__lass__ 指向当前类，所以返回 StringField 和 IntegerField
        # 即调用 StringField(id) 时，返回 <IntegerField:id>
        return '<%s:%s>' % (self.__class__.__name__, self.name)

    # Field('xx') 可打印以上字段
    __repr__ = __str__

class StringField(Field):
    def __init__(self, name):
        # super(StringField,self) 首先找到 FooChild 的父类(Field),然后把类B的对象 StringField 转为 Field 的对象
        # varchar（100） 为最大允许 100 字节
        super(StringField, self).__init__(name, 'varchar(100)')

class IntegerField(Field):
    def __init__(self, name):
        # bigint 为最大整数
        super(IntegerField, self).__init__(name, 'bigint')

class ModelMetaclass(type):

    # 在 __init__ 之前，在类准备将自身实例化时调用，cls 为当前正在实例化的类
    # __new__ 参数为：准备创建的类的对象；类的名字；类继承的父类集合；类的方法集合
    # 如果new()没有返回cls（即当前类）的实例，那么当前类的init()方法是不会被调用的
    # attrs 会将 bar = True, 翻译为 {'bar':True}
    # attrs = {id:<IntegerField:id>,name:<StringField:username>,email:<StringField:email>, password:<StringField:password>}
    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            # 得到当前类的实例，使用父类 xx.__new__(cls）
            # 即运行 Model 类时，调用
            return type.__new__(cls, name, bases, attrs)
        # 运行 User 时调用
        print('Found model:%s' % name)  # 掉那个用后，当前 name 为 User
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('Found mapping:%s==>%s' % (k, v))
                # 使用 mappings 存储 {id:<IntegerField:id>,name:<StringField:username>,email:<StringField:email>, password:<StringField:password>}
                mappings[k] = v
        # mappings.keys(),返回 ['id','name','email','password']
        for k in mappings.keys():
            # 调用 u.save() 时，使 __getattr__ 顺利调用
            attrs.pop(k)
        # attrs 为即将要创建的 class 的属性，attrs['__mappings__'] 相当于
        # class Model(dict):
        #     def __mappings__(self):
        #          ?? return mappings
        attrs['__mappings__'] = mappings  # 保存属性和列的映射关系
        attrs['__table__'] = name  # 假设表名与类名一致 User
        return type.__new__(cls, name, bases, attrs)


class Model(dict,metaclass=ModelMetaclass):
    def __init__(self,**kw):
        super(Model,self).__init__(**kw) # 传入的参数为 dict

    # 首先从类的属性或者父类的属性中找，只有查询不到时，才会到getattrs中查找
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)  # <IntergerField:id> 中的 id
            params.append('?')
            # k 为 id,name,email,password；getattr 返回属性 k 的值，应为被 pop 掉了，所以类的属性和父属性中没有 k
            # 因此调用 __getattr__ ，返回 self[id]，即实例 id=1234 的值 1234，否则返回 <IntegerField:id>
            args.append(getattr(self, k, None))
        # ','.join(list) 就是把 list 中所有字符串，按照逗号链接
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))  # str 返回一个对象的 string 格式，将对象壮话为适合人阅读的形式


class User(Model):
    # 定义类的属性到列的映射,将(id=1234,name='wangker',email='test@orm.org',password='my-pwd')
    # 转换为 id=<IntegerField:id> name=<StringField:username> email=<StringField:email> password=<StringField:password'>
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')

u = User(id=1234, name='wangker', email='test@orm.org', password='my-pwd')
u.save()