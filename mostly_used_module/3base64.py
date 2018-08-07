# -*- coding: utf-8 -*-
import base64

def safe_base64_decode(s): # 此函数解决没等号的字符串解码的问题
    if len(s) % 4:
        s+=(4-len(s)%4)*b'='
    print(s)
    return base64.b64decode(s)

# 测试:
assert b'abcd' == safe_base64_decode(b'YWJjZA==')
assert b'abcd' == safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
assert b'abcd' == safe_base64_decode(b'YWJjZA='), safe_base64_decode('YWJjZA=') # 没理解这个逗号的意义
print('ok')
s=base64.b64decode(b'abcd++//')
print(s)
b=base64.b64encode(s)
print(b)
b=base64.urlsafe_b64encode(s) # urlsafe_编码将‘+’、‘/‘变为’-‘、’_'.以解决+和/在url等中无法作为参数的问题
print(b)