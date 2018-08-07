# -*- coding: utf-8 -*-

# 本机可代理端口包括：1080（sock5，https出现bug）、3128（stunnel，ssl连接，https可用）
# ----来自liaoxuefeng，
from urllib import request
proxy_handler = request.ProxyHandler({'https':'127.0.0.1:1080'})
# proxy_auth_handler = request.ProxyBasicAuthHandler()
# proxy_auth_handler.add_password('realm', 'host', 'username', 'password')
# 上两行代码用于代理服务器需要密码的时候
foropen = request.build_opener(proxy_handler)
with foropen.open('https://www.python.org') as f:
    print(f.read())

# 来自https://www.cnblogs.com/zhaof/p/6910871.html，基本操作
import urllib.request
proxy_handler = urllib.request.ProxyHandler({

    'http': 'http://127.0.0.1:3128',
    'https': 'https://127.0.0.1:3128'
})
opener = urllib.request.build_opener(proxy_handler)
response = opener.open('http://www.python.org')
print(response.read())

# 来自 https://www.cnblogs.com/cocoajin/p/3679821.html
# 基本的网络请求
import urllib.request
# 请求百度网页
resu = urllib.request.urlopen('http://www.baidu.com', data=None, timeout=10)
print(resu.read(300).strip()) # strip函数用于去除字符串中的空格
# 指定编码请求
with urllib.request.urlopen('http://www.baidu.com') as resu:
    print(resu.read(300).decode('GBK').strip())
# 指定编码请求
f = urllib.request.urlopen('http://www.baidu.com')
print(f.read(300).decode('utf-8').strip())

# 发送数据请求，CGI程序处理
# 此段代码缺少test.cgi程序,无法执行
import urllib.request
req = urllib.request.Request(url='http://localhost:8990/cgi-bin/test.cgi',
                             data=b'This data is passed to stdin of the CGI')
f = urllib.request.urlopen(req)
print(f.read().decode('utf-8'))

# PUT请求
# 此段提示缺少PUT方法
import urllib.request
DATA = b'some data'
req = urllib.request.Request(url='http://localhost:8990', data=DATA, method='PUT')
f = urllib.request.urlopen(req)
print(f.status)
print(f.reson)

# 基本的HTTP验证，登录请求 关于add_password的uri参数没搞懂
import urllib.request
# creat an OpenerDirctor with wupport for Basic HTTPAuthentication
auth_handler = urllib.request.HttpBasicAuthHandler()
auth_handler.add_password(realm='PDQ Applicaton',
                          uri='https://mahler:8092/site-updates.py',
                          user='klem',
                          passwd='kadidd!ehopper')
opener = urllib.request.bulid_opener(auth_handler)
# ...and install it globally so it can be used with urlopen
urllib.request.install_opener(opener)
urllib.request.urlopen('http://www.example.com/login.html0')

#z 支持代理方式验证请求
proxy_handler = urllib.request.ProxyHandler({'https':
                                             'http://www.example.com:3128/'})
proxy_auth_handler = urllib.request.ProxyBasicAuthHandler()
proxy_auth_handler.add_password('realm','host','username','password')

opener = urllib.request.build_opener(proxy_handler,proxy_auth_handler)
# This time,rather than install the OpenerDirector, we use it directly:
opener.open('http://www.example.com/login.html')

# 添加 http headers
import urllib.request
req = urllib.request.Request('http://www.example.com/')
req.add_header('Referer', 'http://wwwpython.org/')
r = urllib.request.urlopen(req)

# 添加user-agent
import urllib.request
opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
opener.open('http://www.example.com/')

# 带参数的GET请求
import urllib.request
import urllib.parse
params = urllib.parse.urlencode({'spam': 1, 'eggs': 2, 'bacon': 0})
# print(params)
f = urllib.request.urlopen('http://www.musi-cal.com/cgi-bin/query?%s' % params)
print(f.read().decode('utf-8'))

# 带参数的POST请求
import urllib.request
import urllib.parse
data = urllib.parse.urlencode({'spam': 1, 'eggs': 2, 'bacon':0})
data2 = urllib.parse.urlencode([('spam', 1), ('eggs', 2)])
print('%s\n%s' % (data, data2))
data = data.encode('utf-8') # 或者bytes函数
req = urllib.request.Request('http://requestb.in/xrb182xr')
# adding charset parameter to the Content-Type header
req.add_header('Content-Type', 'application/x-www-form-'
                                   'urlencoded;charset=utf-8')
print(req.headers)
# 以下两个函数未搞懂
print(req.has_header('Content-Type'))
print(req.get_header('Content-type'))
f = urllib.request.urlopen(req, data)               
print(f.read().decode('utf-8'))

# 指定代理方式请求
import urllib.request
proxies = {'http': 'http://proxy.example.com:8080/'}
opener = urllib.request.FancyURLopener(proxies)
f = opener.open('http://www.python.org/')
f.read().decode('utf-8')

# 无添加代理
import urllib.request
opener = urllib.request.FancyURLopener({})
f = opener.open('http://www.python.org/')
f.read().decode('utf-8')


# 以下代码来自：https://www.cnblogs.com/wzjbg/p/6507204.html

# 简单的自定义opener()
import urllib
# 构建一个HTTPHandler 处理器对象，支持HTTP请求
http_handler = urllib.request.HTTPHandler()   # 3.3版本后 urllib2库合并带urllib
# 构建一个HTTPSHandler 处理器对象，支持HTTPS请求
https_handler = urllib.request.HTTPSHandler() # 此对象支持传入参数（debuglevel=1，默认为零）
# 调用 build_opener()方法，创建支持处理HTTP请求的opener对象
opener = urllib.request.build_opener(http_handler, https_handler)
# 构建 Request请求
req = urllib.request.Request('https://www.baidu.com') # 支持两种处理器
# 调用自定义的opener对象的open（）方法，发送request请求
res = opener.open(req)
print(res.read())

# ProxyHandler处理器（代理设置），自定义opener来使用代理
import urllib.request
httpproxy_handler = urllib.request.ProxyHandler({'http': '127.0.0.1:3128'}) # 此端口连接至阿里云服务器
nullproxy_handler = urllib.request.ProxyHandler({})
proxySwitch = True # 定义一个代理开关
# 通过build_handler()方法使用这些代理Handler对象，创建自定义opener对象
# 根据代理是否打开，使用不同的代理模式
if proxySwitch:
    opener = urllib.request.build_opener(httpproxy_handler)
else:
    opener = urllib.request.build_opener(nullproxy_handler)
req = urllib.request.Request('http://www.baidu.com')
res = opener.open(req)
# 如果采用 install_opener(opener) 则全局都采用自定义代理，即包括urlopen函数
print(res.read())

# 随机代理访问网站
import urllib
import random
proxy_list = [
    {'http': '127.0.0.1:3128'},
    {'http': '127.0.0.1:3128'},
    {'http': '127.0.0.1:3128'},
    {'http': '127.0.0.1:3128'},
    {'http': '127.0.0.1:3128'}
]
proxy = random.choice(proxy_list) # 随机选择代理
httpproxy_handler = urllib.request.ProxyHandler(proxy) # 使用选择的代理构建处理器对象
opener = urllib.request.build_opener(httpproxy_handler)
req = urllib.request.Request('http://www.baidu.com')
res = opener.open(req)
print(res.read())

# HTTPPasswordMgrWithDefaultRealm() 主要运用于授权代理和Web客户端账户密码
# ProxyBasicAuthHandler() 代理授权验证
import urllib
user = 'mr_mao_hacker' # 私密代理授权的用户
passwd = 'sffqry9r'    # 私密代理授权的密码
proxyserver = '61.158.163.160:16816' # 私密代理IP
passwdmgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
passwdmgr.add_password(None, proxyserver, user, passwd)
proxyauth_handler = urllib.request.ProxyBasicAuthHandler(passwdmgr) # 带密码，不再使用普通类
opener = urllib.request.build_opener(proxyauth_handler)
req = urllib.request.Request('http://www.baidu.com')
res = urllib.request.urlopen(req)
print(res.read())

# HTTPBasicAuthHandler处理器 Web客户端授权验证
import urllib
user = 'admin'
passwd= 'admin'
webserver = 'http://192.168.0.1'
passwdmgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
passwdmgr.add_password(None, webserver, user, passwd)
httpauth_handler = urllib.request.HTTPBasicAuthHandler(passwdmgr)
opener = urllib.request.build_opener(httpauth_handler)
urllib.request.install_opener(opener)
req = urllib.request.Request('http://192.168.0.1')
res = urllib.request.urlopen(req)
with open('file.html', 'wb') as f:
    f.write(res.read())

# Cookie
# Cookie由变量名和值组成，根据 Netscape公司的规定，Cookie格式如下：
# Set－Cookie: NAME=VALUE；Expires=DATE；Path=PATH；Domain=DOMAIN_NAME；SECURE

# cookielib库和HTTPCookieProcessor处理器
'''
CookieJar：管理HTTP cookie值、存储HTTP请求生成的cookie、向传出的HTTP请求添加cookie的对象。
整个cookie都存储在内存中，对CookieJar实例进行垃圾回收后cookie也将丢失。

FileCookieJar (filename,delayload=None,policy=None)：从CookieJar派生而来，用来创建File
CookieJar实例，检索cookie信息并将cookie存储到文件中。filename是存储cookie的文件名。
delayload为True时支持延迟访问访问文件，即只有在需要时才读取文件或在文件中存储数据。

MozillaCookieJar (filename,delayload=None,policy=None)：从FileCookieJar派生而来，创建
与Mozilla浏览器 cookies.txt兼容的FileCookieJar实例。

LWPCookieJar (filename,delayload=None,policy=None)：从FileCookieJar派生而来，创建与
libwww-perl标准的 Set-Cookie3 文件格式兼容的FileCookieJar实例。
'''
# 1.获取Cookie，并保存到CookieJar()对象中
import urllib
from http import cookiejar

cookiejar_new = cookiejar.CookieJar() # 构建一个CookieJar实例来保存cookie
handler = urllib.request.HTTPCookieProcessor(cookiejar_new) # 用函数来创建cookie处理器对象，参数为上述实例
opener = urllib.request.build_opener(handler) # 构建opener
opener.open('http://www.baidu.com') # GET网页，cookie自动保存到cookiejar_new对象中
cookieStr = ''
for item in cookiejar_new: # 可以按照标准格式将保存的Cookie打印出来
    print(item) # 查看数据结构
    cookieStr = cookieStr +item.name + '=' + item.value + ';'
print(cookieStr[:-1])
# 2.访问网站获得cookie，并将获得的cookie保存在cookie文件中
from http import cookiejar
import urllib
filename = './mostly_used_module/cookie.txt' # 保存cookie的本地磁盘文件名
cookiejar_new = cookiejar.MozillaCookieJar(filename) # MozillaCookieJar对象实例，有save实现
handler = urllib.request.HTTPCookieProcessor(cookiejar_new) # 使用该函数chaugnjiancookie处理器对象，参数为CookieJar对象
opener = urllib.request.build_opener(handler) # 构建opener
res = opener.open('http://www.baidu.com')
cookiejar_new.save() #保存cookie到本地文件
# 3.从文件中获取cookies，作为请求的一部分去访问
from http import cookiejar
import urllib
coo = cookiejar.MozillaCookieJar() # 创建MozillaCookieJar对象（有load实现）
coo.load('./mostly_used_module/cookie.txt') # 从文件中读取cookie到变量
handler = urllib.request.HTTPCookieProcessor(coo) # 创建cookie处理器对象，参数为CookieJar对象
opener = urllib.request.build_opener(handler)
res = opener.open('http://www.baidu.com')
# 利用cookiejar和post登录人人网
import urllib
from http import cookiejar
coo = cookiejar.CookieJar() # 用来临时保存cookie
cookie_handler = urllib.request.HTTPCookieProcessor(coo) # 创建cookie处理器对象
opener = urllib.request.build_opener(cookie_handler)
opener.addheaders=[("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                                  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36")]
# addheaders接收一个列表，里面每个元素都是一个headers信息的元组，opener将附带headers信息
data={'email': '15111171986', 'password': 'ls950322'} # 需要登录的账户名与密码
postdata = urllib.parse.urlencode(data).encode('utf-8') # 对data信息进行转码
req = urllib.request.Request('http://www.renren.com/PLogin.do', data = postdata)
opener.open(req) # 通过opener发送请求，并获取登录后的cookie值
res = opener.open('http://www.renren.com/410043129/profile') # 利用登录后的cookie进入权限网页
z = res.read()
print(z) # 打印响应内容
with open('./mostly_used_module/renren.html', 'wb') as f:
    f.write(z)