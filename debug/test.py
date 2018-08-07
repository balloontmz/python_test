import logging
# 定义日志级别
logging.basicConfig(level=logging.ERROR)
s = '0'
n = int(s)
# assert n !=0,'n is zero'
# 可以通过-O参数来关闭assert
# 输出错误，或者可以输出到文件
logging.error('n={0}'.format(n))
print('100')