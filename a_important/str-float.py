# -*- coding: utf-8 -*-
from functools import reduce

def str2float(s):
    def char_num(z):
        dick={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
        return dick[z]
    def num_qua1(x,y):
        return x*10+y
    def num_qua2(m,n):
        return m*0.1+n
    s1,s2=s.split('.')
    s2=s2[::-1]
    return reduce(num_qua1,map(char_num,s1))+reduce(num_qua2,map(char_num,s2))*0.1
    #return reduce(lambda x,y:x*10+y,map(char_num,s1))+reduce(lambda x,y:x*0.1+y,map(char_num,s2))*0.1 简化形式

print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')


