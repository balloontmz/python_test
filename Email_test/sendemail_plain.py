from email.mime.text import MIMEText

msg = MIMEText('Hello, send by Python...', 'plain', 'utf-8')

# 输入Email地址和口令：
from_addr = '1956354744@qq.com'
password = 'omupscibflcfbfaa'
# 输入收件人地址：
to_addr = '15111171986@163.com'
# 输入SMTP服务器地址：
smtp_server = 'smtp.qq.com'

import smtplib
server = smtplib.SMTP(smtp_server, 25) # SMTP协议默认端口为25
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()