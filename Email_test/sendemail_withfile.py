from email import encoders
from email.header import Header
from email.mime.text import MIMEText # mime:多用途互联网邮件拓展
from email.utils import parseaddr, formataddr # utils: 工具
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase

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

# 邮件对象
msg = MIMEMultipart()
msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('来自STMP的问候...', 'utf-8').encode()
print(msg)

# 邮件正文是MIMEText:
msg.attach(MIMEText('send with file...', 'plain', 'utf-8')) # 文本文件

# 添加附件就是加上一个MIMEBase，从本地读取一个图片：
with open('1.png', 'rb') as f:
    # 设置附件的MIME和文件名，这里png类型：
    mime = MIMEBase('image', 'png', filename='3.png') # 此个filename没必要？
    # 加上必要的头信息：
    mime.add_header('Content-Disposition', 'attachment', filename='3.png')
    #mime.add_header('Content-ID', '<image0>')
    #mime.add_header('X-Attachment-Id', '1') # 此行意义没了解,猜测可能用于附件队列
    print(mime)
    # 把附件内容添加进来：
    mime.set_payload(f.read())
    # 用Base64编码：
    encoders.encode_base64(mime)
    # 添加到MIMEMultipart
    msg.attach(mime)

print('*' * 50)
# print(msg)

#######################################################################################################################
import smtplib
server = smtplib.SMTP(smtp_server, 25) # SMTP协议默认端口为普通25 SMTP_SSL 465  starttls()587 后两中为加密端口
server.starttls()
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()