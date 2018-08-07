from io import StringIO

f = StringIO('Hello World') #初始化完文件指针回到了0
print('StringIO position ='+str(f.tell()))
f.write('asdf') #写入数据后，文件指针停在当前位置
f.write('asdf') #写入数据后，文件指针停在当前位置
print('write position ='+str(f.tell()))
f.seek(0) #文件指针回到初始位置
s = f.read()
print(s)