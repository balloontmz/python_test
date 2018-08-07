# -*- coding: utf-8 -*-


class Dict(dict):

    def __init__(self,**kw):
        super().__init__(self,**kw)

    def __getattr__(self, item):
        try:
            return self[item]
        except KeyError:
            raise AttributeError("'Dict' has no attribute of '{0}'".format(item))  # AttributeError 将与后文单元测试需要一致

    def __setattr__(self, key, value):  # 此操作把键值写入列表，而不单纯只是写属性
        self[key] = value


d = Dict(a=1, b=2)