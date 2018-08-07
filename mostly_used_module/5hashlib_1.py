# -*- coding: utf-8 -*-

import hashlib

db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}
def login(usr, pw):
    usr_pw = db[usr]
    z = hashlib.md5(pw.encode('utf-8')).hexdigest() # 创建一个md5实例并调用它的hexdigest方法
    return z == usr_pw

def login_2(usr, pw):
    usr_pw = db[usr]
    md = hashlib.md5()
    md.update(pw.encode('utf-8')) # 调用实例的方法
    return md.hexdigest() == usr_pw

# 测试:
assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
assert login_2('michael', '123456')
print('ok')