import subprocess

print('$ nslookup')
p = subprocess.call(['nslookup', 'www.python.org'])
print('Exit code:', p)
# 很多时候，子进程并不是自身，而是一个外部进程，所以我们在创建了子进程之后，还需要控制子进程的输入和输出
# subprocess.Popen用来创建新的进程
# shell=True 表示在系统默认的shell环境中执行新的进程，windows下为cmd，linux下为/bin/sh
# executable 表示当shell为True时，用executable来修改默认的shell环境
# 默认的stdin,stdout,stderr均为None，表示新进程的stdin，stdout，stderr均为默认，从keyboard获得输入，将输出和错误输出到display
# 而如果stdin,stdout,stderr为PIPE，则表示打开了一个管道至标准流
# universal_newlines,如果为True，那么所有的行结束符会被转换成对应系统平台的换行符
# Popen.communicate(input=None) 与进程交互，将数据发送到标准输入
