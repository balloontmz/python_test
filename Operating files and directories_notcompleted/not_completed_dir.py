import os
import time

# 来自评论区， dir的简单实现
input_str = input(">>").split()
if input_str[0] == 'dir':
    abs_path = os.path.abspath('.')
    dir_list = os.listdir('.')
    for i in dir_list:
        fpath = os.path.join(abs_path,i)
        fsize = os.path.getsize(fpath)
        fctime = time.gmtime(os.path.getctime(fpath))
        ftimestamp = time.strftime('%Y/%m/%d %H:%M:%S',fctime)
        if os.path.isfile(fpath):
            if_dir = ' '
        else:
            if_dir = '<DIR>'
        print(ftimestamp,fsize,if_dir,i,'\n')