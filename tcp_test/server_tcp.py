import socket
import threading
import time
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 准备监听窗口
s.bind(('0.0.0.0', 9999)) # 0.0.0.0表示全部ip，127.0.0.1表示本地ip，只能本地访问
# 开始监听
s.listen(5) # 5代表最大连接数
print('Waiting for Connection...')


def tcplink(sock1, addr2): # 处理连接的函数，可以打印参数查看其属性（addr是一个二元素truple）
    print('Accpet new Connection from %s:%s...' % addr2)
    sock1.send(b'Welcome')
    while True:
        data = sock1.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock1.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock1.close()
    print('Connection from %s:%s closed' % addr2)


while True:
    # 接受一个新连接
    sock, addr = s.accept()
    # 创建线程来处理TCP连接
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()
