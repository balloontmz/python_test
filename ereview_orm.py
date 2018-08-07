#!/user/bin/env python3
# -*- coding: utf-8 -*-

"""a easy orm"""

__anthor__ = 'tomtiddler'


class Field(object):

    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<%s : %s>' % (self.__class__.__name__, self.name)
    __repr__ = __str__


class StringField(Field):

    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')


class InterField(Field):

    def __init__(self, name):
        super(InterField, self).__init__(name, 'bigint')


class ModelMetaclass(type):

    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return super(ModelMetaclass, cls).__new__(cls, name, bases, attrs)
        mapping = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('%s ==> %s' % (k, v))
            mapping[k] = v
        for k in mapping.keys():
            attrs.pop(k)
        attrs['__mapping__'] = mapping
        attrs['__table__'] = name
        return super(ModelMetaclass, cls).__new__(cls, name, bases, attrs)


class Model(dict, metaclass=ModelMetaclass):

    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, item):
        try:
            return self[item]
        except KeyError:
            raise ArithmeticError(r"'Model' has no attrbute as '%s" % item)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        a = []
        b = []
        c = []
        for key, value in self.__mapping__.items():
            if isinstance(value, Field):
                a.append(value.name)
                b.append('?')
                c.append(getattr(self, key, None))
        sql = 'INSERT TO %s (%s) values (%s)' % (self.__class__.__name__, ','.join(a), ','.join(b))
        print('SQL:%s' %sql)
        print('ARGS: [%s]' % str(c))


class User(Model):
    id = InterField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')


u = User(id=12345, name='tom', email='15111171986@163.com', password='ls950322')
u.save()
