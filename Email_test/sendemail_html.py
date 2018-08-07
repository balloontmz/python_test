from email import encoders
from email.header import Header
from email.mime.text import MIMEText # mime:多用途互联网邮件拓展
from email.utils import parseaddr, formataddr # utils: 工具

# 输入Email地址和口令：
from_addr = '15111171986@163.com'
password = 'tang19940807'
# 输入收件人地址：
to_addr = '1956354744@qq.com'
# 输入SMTP服务器地址：
smtp_server = 'smtp.163.com'


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))
msg = MIMEText('<html><body><h1>Hello</h1><p>send by <a href='
               '"http://www.python.org">python</a>...</p></body><html>',
               'html', 'utf-8') # html邮件构造
# msg = MIMEText('Hello, send by Python...', 'plain', 'utf-8') # 文本邮件
# 加上Header之后能使用163了，不报554错误了。
msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('来自STMP的问候...', 'utf-8').encode()
print(msg)

import smtplib
server = smtplib.SMTP(smtp_server, 25) # SMTP协议默认端口为25 465 587
server.starttls()
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()