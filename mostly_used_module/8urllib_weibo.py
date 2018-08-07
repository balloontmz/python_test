# -*- coding: utf-8 -*-
# 微博登录
from urllib import request, parse

dict_ = {'Host': 'passport.weibo.cn',
         'Connection': 'keep-alive',
         'Content-Length': '173',
         'Origin': 'https://passport.weibo.cn',
         'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                       'Chrome/67.0.3396.99 Safari/537.36',
         'Content-Type': 'application/x-www-form-urlencoded',
         'Referer': 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F',
         # 'Accept-Encoding': 'gzip, deflate, br'. # 此词条来自抓包，造成了程序错误
         'Accept-Language': 'zh-CN,zh;q=0.9'
         }

data = b'username=15111171986&password=ls950322&savestate=1&r=http%3A%2F%2Fm.weibo.cn%2F&ec=0' \
       b'&pagerefer=&entry=mweibo&wentry=&loginfrom=&client_id=&code=&qq=&mainpageflag=1&hff=&hfp='
# data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='utf8')
# 关于parse的用法，此程序数据直接取自抓包，未采用传入data的方法。
# parse用来抓换数据（bytes方法相当于encode方法）
print('Login to weibo.cn...')
print(parse.urlencode(dict_))
# 关于parse的使用，将dict_转换为data

req = request.Request('https://passport.weibo.cn/sso/login')
for k in dict_:
    req.add_header(k, dict_[k])

with request.urlopen(req, data=data) as f:
    print('Status', f.status, f.reason)
    for m, n in f.getheaders():
        print('%s: %s' % (m, n))
    print('Data:', f.read().decode(encoding='utf-8'))

