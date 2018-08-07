# -*- coding: utf-8 -*-
# 实现了服务端 与 客户端的 分离，采用json为交换格式，db(本例中可去掉）仅仅保存在服务端
# 采用hmac也能运行
import hashlib, random, json, hmac

def hmac_md5(key, str):
    return hmac.new(key.encode('utf-8'), str.encode('utf-8')).hexdigest()


class User(object):
    def __init__(self, usr, pw):
        self.usr = usr
        self.salt = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        self.password = hmac_md5(self.salt, pw)

db = {}

def register(usr, pw):
    db[usr] = User(usr, pw) # db 可去掉
    with open('/home/tomtiddler/Documents/python_test/tom2.txt', 'a') as f:
        json.dump(db[usr], f, default=lambda obj: obj.__dict__)
        f.write('\n') # 罪魁祸首，打开tom情况下运行会多一个'\n'导致读取时无法判定为json格式


def login(usr, pw):
    with open('/home/tomtiddler/Documents/python_test/tom2.txt', 'r') as f:
        for lines in f.readlines():
            user = json.loads(lines.strip()) # 提取json文件作为user属性的dict
            if user['usr'] == usr:
                break
    return user['password'] == hmac_md5(user['salt'], pw)



register('bob', 'abc999')
register('alice', 'alice2008')
register('michael', '123456')
print(db['michael'].salt) # salt是变化的  但是，login取的是salt的空间，而不是固定的值。
# 测试:

assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')
print(chr(random.randint(48, 122))) # 某个符号？
print(db['michael'].salt)
print([(x, chr(x)) for x in range(48,123)]) # 一个简单的编码表？？？