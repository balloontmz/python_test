# -*- coding: utf-8 -*-
import io
import struct
import base64


with open('/home/tomtiddler/Documents/python_test/test_.bmp', 'rb') as f:
    b = f.read(30) # 文件指针向后挪动了
    f.seek(0) # 文件指针的重置
    c = f.read(60)

# bmp 采用little-endian字节序
one = struct.unpack('<ccIIIIIIHH', b) # little-endian
two = struct.unpack('>ccIIIIIIHH', b) # big-endian
print(one)
print(two)
print(struct.unpack('<ccIIIIIIHH', c[:30])) # c是字符串，能够slice
print(base64.b64encode(c)) # 这篇有复习
print(type(c))
print(isinstance(c, str))
print(isinstance(base64.b64encode(c), str))


bmp_data = base64.b64decode('Qk1oAgAAAAAAADYAAAAoAAAAHAAAAAoAAAABABAAAAAAADICAAASCw'
                            'AAEgsAAAAAAAAAAAAA/3//f/9//3//f/9//3//f/9//3//f/9//3//f'
                            '/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9/AHwAfAB8AHwAf'
                            'AB8AHwAfP9//3//fwB8AHwAfAB8/3//f/9/AHwAfAB8AHz/f/9//3//f'
                            '/9//38AfAB8AHwAfAB8AHwAfAB8AHz/f/9//38AfAB8/3//f/9//3//fw'
                            'B8AHz/f/9//3//f/9//3//f/9/AHwAfP9//3//f/9/AHwAfP9//3//fwB8'
                            'AHz/f/9//3//f/9/AHwAfP9//3//f/9//3//f/9//38AfAB8AHwAfAB8AH'
                            'wAfP9//3//f/9/AHwAfP9//3//f/9//38AfAB8/3//f/9//3//f/9//3//'
                            'fwB8AHwAfAB8AHwAfAB8/3//f/9//38AfAB8/3//f/9//3//fwB8AHz/f/'
                            '9//3//f/9//3//f/9/AHwAfP9//3//f/9/AHwAfP9//3//fwB8AHz/f/9/A'
                            'Hz/f/9/AHwAfP9//38AfP9//3//f/9/AHwAfAB8AHwAfAB8AHwAfAB8/3//f'
                            '/9/AHwAfP9//38AfAB8AHwAfAB8AHwAfAB8/3//f/9//38AfAB8AHwAfAB8A'
                            'HwAfAB8/3//f/9/AHwAfAB8AHz/fwB8AHwAfAB8AHwAfAB8AHz/f/9//3//f'
                            '/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//'
                            '3//f/9//38AAA==')
def bmp_info(data):
    if len(data) >=30:
        L = struct.unpack('<ccIIIIIIHH',data[:30])
        if L[0] == b'B' and L[1] == b'M':
            print(L)
            return {'width': L[6],'height': L[7],'color': L[9]}
        else:
            return '此文件不是位图'
    else:
        return '该文件不是位图文件'
# 测试
bi = bmp_info(bmp_data)
assert bi['width'] == 28
assert bi['height'] == 10
assert bi['color'] == 16
print('ok')