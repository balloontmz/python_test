import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接
s.connect(('120.79.157.29', 9999))
# 接收欢迎信息
print(s.recv(1024).decode('utf-8'))
for data in [b'michael', b'tracy', b'sarah']:
    # 发送数据
    s.send(data)
    print(s.recv(1024).decode('utf-8'))
s.send(b'exit')
s.close()
